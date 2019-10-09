from flask import *
from flask_restful import Resource
from model.ShortUrlAccess import ShortUrlAccess

# TODO: maybe implement a check to see whether the short url actually exists


class ReadShortUrl(Resource):
    def post(self):
        data = request.get_json()
        short_url = data["short_url"]

        # save to DB
        ShortUrlAccess(
            short_url = short_url
        ).save()

        return {'response': 'OK'}