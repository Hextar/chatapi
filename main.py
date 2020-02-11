import logging
from os import environ
from flask import Flask, render_template

from flask_marshmallow import Marshmallow
from flask_restful import Api

from flask_socketio import SocketIO

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.DEBUG)

APP = Flask(__name__)
APP.secret_key = 'secret!$#'
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

API = Api(APP)
MA = Marshmallow(APP)
SETTINGS = APP.config

DB = SQLAlchemy(APP)

login_manager = LoginManager()
login_manager.login_view = "signin"
login_manager.init_app(APP)

socketio = SocketIO(APP)

# flask routes
from app.handlers.socket import *
from app.handlers.room import *
from app.handlers.signin import *
from app.handlers.logout import *

# flask loaders
from app.loaders import load_user

# sqlalchemy models
from app.models.user import User
from app.models.room import Room
from app.models.message import Message

# flask restful resources
from app.api import BotResource
API.add_resource(BotResource, '/api/v1/bot')

if __name__ == '__main__':
    socketio.run(APP, debug=True)

