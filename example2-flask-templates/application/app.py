import logging
import awsgi
import logging
from flask import Flask, render_template
from flask.helpers import url_for

app = Flask(__name__, instance_relative_config=True)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# app.config.from_object('config.Config')

from flask_static_digest import FlaskStaticDigest

flask_statics = FlaskStaticDigest(app=app)

@app.route('/')
def index():
    logger.debug(app.config)
    logger.debug(url_for('static', filename='materialize.css'))
    return render_template('index.html')

def lambda_handler(event, contex):
    return awsgi.response(app, event, contex)
