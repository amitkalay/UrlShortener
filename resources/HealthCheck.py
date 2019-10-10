from flask_restful import Resource
from model.SimpleDataModel import SimpleDataModel


class HealthCheck(Resource):
    def get(self):
        return {'healthcheck': 'OK'}
