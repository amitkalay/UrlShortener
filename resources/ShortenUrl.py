from flask import *
from flask_restful import Resource
import random
import string

class ShortenUrl(Resource):
    # ONLY accepts content type as application/json
    def post(self):
        data = request.get_json()
        #generate the short URL by creating a random string that's 10 characters long
        short_url = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
        data["short_url"] = short_url
        # TODO: persist to a database
        return jsonify(data)
