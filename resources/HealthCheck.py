from flask_restful import Resource
from model.ShortUrlAccess import ShortUrlAccess
from datetime import datetime
from datetime import timedelta


class HealthCheck(Resource):
    def get(self):
        return {'healthcheck': 'OK'}


"""
        ShortUrlAccess(short_url='test',
                       date_accessed = datetime.now() - timedelta(weeks=2)
                       ).save()

        ShortUrlAccess(short_url='test',
                       date_accessed=datetime.now() - timedelta(weeks=3)
                       ).save()


        ShortUrlAccess(short_url='test',
                       date_accessed=datetime.now()
                       ).save()
        """
