from os import environ
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_marshmallow import Marshmallow
from flask_restful import Api

APP = Flask(__name__)
APP.config.from_pyfile(environ.get('CONFIG_FILE'))
DB = SQLAlchemy(APP)
migrate = Migrate(APP, DB)

manager = Manager(APP)
manager.add_command('db', MigrateCommand)

API = Api(APP)
MA = Marshmallow(APP)
SETTINGS = APP.config

from app.models import *

@APP.route("/")
def index():
    """Root route.
    Returns:
        Str: Simple hello world response
    """
    return "Hello World!"

