import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    response = request.args['response']
    try:
        return "Your response is: " + response
    except KeyError:
        return f'Invalid response'
        
