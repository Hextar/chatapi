import logging
from os import environ
from flask import Flask, render_template

from flask_marshmallow import Marshmallow
from flask_restful import Api

from flask_socketio import SocketIO

from flask_login import LoginManager

logging.basicConfig(level=logging.DEBUG)

APP = Flask(__name__)
APP.secret_key = 'secret!$#'

API = Api(APP)
MA = Marshmallow(APP)
SETTINGS = APP.config

login_manager = LoginManager()
login_manager.login_view = "signin"
login_manager.init_app(APP)

socketio = SocketIO(APP)

from app.handlers.socket import *
from app.handlers.room import *
from app.handlers.signin import *
from app.handlers.logout import *

from app.loaders import load_user

from app.api import BotResource

API.add_resource(BotResource, '/api/v1/bot')

if __name__ == '__main__':
    socketio.run(APP, debug=True)

