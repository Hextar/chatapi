from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_marshmallow import Marshmallow
from flask_restful import Api

APP = Flask(__name__)
APP.config.from_object(Config)
DB = SQLAlchemy(APP)
migrate = Migrate(APP, DB)

API = Api(APP)
MA = Marshmallow(APP)
SETTINGS = APP.config

@APP.route("/")
def index():
    """Root route.
    Returns:
        Str: Simple hello world response
    """
    return "Hello World!"

