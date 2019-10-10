from flask_restful import Resource
from flask import *
from model.UrlInfo import UrlInfo


class LongUrl(Resource):
    url_cache = dict()

    def post(self):
        data = request.get_json()
        if "short_url" not in data:
            return {'error': 'need a short_url key-value pair in the payload'}, 500

        # try hitting the cache
        input_short_url = data["short_url"]
        if input_short_url in self.url_cache:
            print("the url was in the cache!")
            long_url = self.url_cache[input_short_url]
            response = dict()
            response["short_url"] = input_short_url
            response["long_url"] = self.url_cache[input_short_url]
            # TODO: persist this request to the short_url accesses tables so we can count this as a "hit"
          #  UrlInfo(
          #      short_url=input_short_url,
          #      long_url=long_url
          #  ).save()
            return jsonify(response)

        # otherwise pull the long url from the database and return that in the response
        else:
            url_info = UrlInfo.objects(short_url=input_short_url)

            for doc in url_info:
                return {
                    'short_url': doc.short_url,
                    'long_url': doc.long_url
                }
                #print(doc)

        # if we have nothing in the database for that short url, it didn't exist
        return {'error': 'That short url was never created'}, 404
