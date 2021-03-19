import logging
import logging
import myawsgi
from flask import Flask, render_template, request
from flask.helpers import url_for
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def create_app(config='config.Config'):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    from flask_static_digest import FlaskStaticDigest

    flask_statics = FlaskStaticDigest(app=app)

    @app.route('/otra')
    def otra():
        return "In otra function"

    @app.route('/')
    def index():
        logger.debug(app.config)
        logger.debug(flask_statics.static_url_for('static', filename='materialize.css'))
        logger.debug(url_for('static', filename='materialize.css', _external=True))
        logger.debug(url_for('otra'))
        logger.debug(url_for('otra', _external=True))
        logger.debug(request.path)
        logger.debug(request.host)
        logger.debug(request.host_url)
        logger.debug(request.full_path)
        return render_template('index.html')

    return app


def lambda_handler(event, contex):
    logger.debug(f"EVENT: {event}")
    app = create_app()
    return myawsgi.response(app, event, contex)
