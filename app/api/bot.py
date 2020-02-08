import json
import logging
from flask_restful import Resource
from webargs.flaskparser import use_args

from main import API

class BotResource(Resource):
    """Bots Endpoint to manage request from Sendbird platform."""

    def post(self):
        return 'ok'
        
API.add_resource(
    BotResource,
    '/api/v1/bot')