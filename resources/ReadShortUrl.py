from flask import *
from flask_restful import Resource
from model.ShortUrlAccess import ShortUrlAccess


class ReadShortUrl(Resource):
    def post(self):
        data = request.get_json()
        short_url = data["short_url"]

        # save to DB
        ShortUrlAccess(
            short_url = short_url
        ).save()

        return {'response': 'the short url: ' + short_url + ' was accessed'}