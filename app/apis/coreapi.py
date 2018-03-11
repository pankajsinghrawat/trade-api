from flask import Blueprint
from flask_restplus import Api
from flask_restplus import Resource
from business.business import trade
import json

coreapiblueprint = Blueprint('coreapi', __name__)
coreapi = Api(coreapiblueprint)

nscoreapi = coreapi.namespace('trade', description='Trade APIs')

@nscoreapi.route('/start')
class startTrade(Resource):
    def get(self):
        trade(True)
        return {'message': 'Trade Started'}

@nscoreapi.route('/stop')
class stopTrade(Resource):
    def get(self):
        trade(False)
        return {'message': 'Trade Stopped'}
