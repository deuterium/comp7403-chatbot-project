from flask import Flask, request, make_response, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    try:
        intent = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'
    print("Intent: {}".format(intent))
    # if action == 'weather':
    #     res = weather(req)
    # elif action == 'weather.activity':
    #     res = weather_activity(req)
    # elif action == 'weather.condition':
    #     res = weather_condition(req)
    # elif action == 'weather.outfit':
    #     res = weather_outfit(req)
    # elif action == 'weather.temperature':
    #     res = weather_temperature(req)
    # else:
    #     log.error('Unexpected action.')

    # print('Action: ' + action)
    # print('Response: ' + res)

    return make_response(jsonify({'fulfillmentText': "intent {}".format(action)}))

if __name__ == "__main__":
    app.run()
