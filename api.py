from flask import Flask
from flask_restful import Resource, Api
from resources.HealthCheck import HealthCheck
from resources.ShortenUrl import ShortenUrl
from resources.LongUrl import LongUrl
import mongo_setup as mgo

"""
Installation:
pip install flask
pip install flask-restful
Install the actual mongo from the website
pip install mongoengine
"""

app = Flask(__name__)
api = Api(app)

mgo.global_init()

api.add_resource(HealthCheck, '/healthcheck')
api.add_resource(ShortenUrl, '/shorten')
api.add_resource(LongUrl, '/getlong')

if __name__ == '__main__':
    app.run(debug=True)
