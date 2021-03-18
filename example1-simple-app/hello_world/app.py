import awsgi
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !!!"

def lambda_handler(event, contex):
    return awsgi.response(app, event, contex)
