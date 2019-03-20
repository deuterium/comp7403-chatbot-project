from flask import Flask, request, jsonify
#import dialogflow
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World2!'

@app.route('/test-fullfillment', methods=['POST'])
def test_fullfillment():
    # data = request.get_json(silent=True)
    
    try:
        # movie = data['queryResult']['parameters']['movie']
        # api_key = os.getenv('OMDB_API_KEY')
        
        # movie_detail = requests.get('http://www.omdbapi.com/?t={0}&apikey={1}'.format(movie, api_key)).content
        # movie_detail = json.loads(movie_detail)

        response =  """
            Title : {0}
            Released: {1}
            Actors: {2}
            Plot: {3}
        """.format("Great movie title!!!", "2020", "Bruce Willis", "Adam Sandlar", "G.I. Joe", "Take a gander at your favourite heros back at it again in this blockbuster hit of the summmer")
    except:
        response = "Could not get movie detail at the moment, please try again"
    
    reply = {
        "fulfillmentText": response,
    }
    
    return jsonify(reply)


if __name__ == "__main__":
    app.run()