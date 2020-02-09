import json
import logging
from flask_restful import Resource
from webargs.flaskparser import use_args

class BotResource(Resource):
    """Bots Endpoint to manage request from Sendbird platform."""

    def post(self):
        return 'ok'