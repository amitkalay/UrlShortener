from flask import Flask
from flask_restful import Resource, Api
from resources.HealthCheck import HealthCheck
from resources.ShortenUrl import ShortenUrl
from resources.LongUrl import LongUrl
from resources.ReadShortUrl import ReadShortUrl
import mongo_setup as mgo

"""
Installation:
pip install flask
pip install flask-restful
Install the actual mongo from the website
pip install mongoengine
create the database collections all_urls and short_url_access
"""

app = Flask(__name__)
api = Api(app)
# initialize db connection
mgo.global_init()

api.add_resource(HealthCheck, '/healthcheck')
api.add_resource(ShortenUrl, '/shorten')
api.add_resource(LongUrl, '/getlong')
api.add_resource(ReadShortUrl, '/shortaccess')

if __name__ == '__main__':
    app.run(debug=True)
