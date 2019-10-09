from flask_restful import Resource
from model.SimpleDataModel import SimpleDataModel


class HealthCheck(Resource):
    def get(self):
        simp = SimpleDataModel(
            name='aRealPerson',
            num=45
        ).save()
        return {'healthcheck': 'OK'}
