from flask import Flask, request, jsonify
import os
#import dialogflow
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World2!'





if __name__ == "__main__":
    app.run()