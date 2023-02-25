from flask import Flask, request
from src.users import get_users
from src.user import info
from src.sentiment_analysis import get_sentiment
from src.get_followers_count import get_followers_count
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():
    return 'Flask is running!'

@app.route('/users', methods = ['POST' , 'GET'])
def users():
    print("Got request for users")
    return get_users()

@app.route('/user_info', methods = ['POST', 'GET'])
def user_info():
    print("Got request for user info")
    user_id = request.json['user_id']
    # print(user_id)
    return info(user_id)

@app.route('/sentiment', methods=['POST', "GET"])
@cross_origin()
def senti():
    print("Got request for sentiment")
    text = request.json['text']
    return get_sentiment(text)

@app.route('/followers_count', methods=['POST', "GET"])
def followers_count():
    print("Got request for followers count")
    user_name = request.json['user_name']
    return get_followers_count(user_name)

if __name__ == '__main__':
    app.run(debug=True)
