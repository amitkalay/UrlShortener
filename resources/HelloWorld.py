from flask_restful import Resource
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'Srinath'}

#api.add_resource(HelloWorld, '/helloworld')
