from flask import *
from flask_restful import Resource
import random
import string
from resources.LongUrl import LongUrl
from model.UrlInfo import UrlInfo


class ShortenUrl(Resource):
    # ONLY accepts content type as application/json
    def post(self):
        data = request.get_json()
        # return a 500 response if a long url wasn't provided to begin with
        if "long_url" not in data:
            return {'error': 'Please provide a long_url key-value pair in the payload'}, 500
        # generate the short URL by creating a random string that's 10 characters long
        long_url = data["long_url"]
        short_url = self.generate_short_url(10)
        data["short_url"] = short_url

        # store the URL in our cache
        LongUrl.url_cache[short_url] = long_url

        UrlInfo(
            short_url=short_url,
            long_url=long_url
        ).save()
        return jsonify(data)

    def generate_short_url(self, length: int) -> string:
        short_url = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
        return short_url
