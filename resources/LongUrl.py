from flask_restful import Resource
from flask import *

class LongUrl(Resource):
    url_cache = dict()
    #def __init__(self):
    #    pass
    def post(self):
        data = request.get_json()
        if "short_url" not in data:
            return {'error': 'need a short_url key-value pair in the payload'}, 500


        # try hitting the cache
        short_url = data["short_url"]
        if short_url in self.url_cache:
            print("the url was in the cache!")
            response = dict()
            response["short_url"] = short_url
            response["long_url"] = self.url_cache[short_url]
            # persist this request to the db so we can count on it later
            UrlInfo(
                short_url=short_url,
                long_url=long_url
            ).save()
            return jsonify(response)

        return {'default': 'response'}
