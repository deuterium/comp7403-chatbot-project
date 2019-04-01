from flask import Flask, request, make_response, jsonify
from loguru import logger
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    try:
        intent = req.get('queryResult').get('intent').get('displayName')
    except AttributeError:
        return 'json error'

    logger.debug("Full Request: \n {}", req)
    logger.debug("Intent: {}", intent)

    if intent == 'top2':
        res = "{}\n{}".format(scrape('LOVEYY'),scrape('CD996M'))
    elif intent == 'lookupPlate':
        res = scrape(req.get('queryResult').get('parameters').get('any'))
    else:
        err = 'Unexpected action.'
        logger.error(err)
        res = err

    return make_response(jsonify({'fulfillmentText': res}))

def scrape(plate):
    if re.match("^[a-zA-Z0-9]{2,6}$", plate) is None:
        return "Please request a valid plate number. (Min: 2, Max: 6)"

    cookies_url = "https://payments.impark.com"
    url = "https://payments.impark.com/Notice/?lp={}&ps=BC".format(plate)

    headers = {'Host': 'payments.impark.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Referer': 'https://payments.impark.com/Home/Search?q=license', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9'}
    cookies_req = requests.post(cookies_url)

    resp = requests.get(url, headers=headers, cookies=cookies_req.cookies)
    html = BeautifulSoup(resp.content, 'html.parser')

    rst = html.select("td.noticeNum")

    ticket_amounts = html.select("td.amount")
    total = 0
    for t in ticket_amounts:
        total += float(t.text.strip().replace('$',''))

    logger.debug("plate: {} tickets: {} amount: {}", plate, len(rst), total)

    if len(rst) == 0:
        return "There are no parking tickets for {}.".format(plate)
    else:
        return "{} has {} parking tickets owing {}.".format(plate, len(rst), '${:,.2f}'.format(total))

if __name__ == "__main__":
    app.run()
