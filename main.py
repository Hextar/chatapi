import logging
from os import environ
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_marshmallow import Marshmallow
from flask_restful import Api

from flask_socketio import SocketIO

from app.api import BotResource
logging.basicConfig(level=logging.DEBUG)

APP = Flask(__name__)
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

DB = SQLAlchemy(APP)
migrate = Migrate(APP, DB)

manager = Manager(APP)
manager.add_command('db', MigrateCommand)

API = Api(APP)
MA = Marshmallow(APP)
SETTINGS = APP.config

socketio = SocketIO(APP)

from app.models import *

@APP.route("/")
def hello():
    """Root route.
    Returns:
        Str: Simple hello world response
    """
    return "Hello World!"

API.add_resource(BotResource, '/api/v1/bot')

if __name__ == '__main__':
    socketio.run(APP, debug=True)

