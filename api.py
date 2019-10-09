from flask import Flask
from flask_restful import Resource, Api
from resources.HealthCheck import HealthCheck
from resources.ShortenUrl import ShortenUrl
from resources.LongUrl import LongUrl

app = Flask(__name__)
api = Api(app)

api.add_resource(HealthCheck, '/healthcheck')
api.add_resource(ShortenUrl, '/shorten')
api.add_resource(LongUrl, '/getlong')

if __name__ == '__main__':
    app.run(debug=True)
