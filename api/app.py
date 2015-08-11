from flask import Flask
from flask_restful import Api
from api.v1.resources.ping import Ping


app = Flask(__name__)
app.config.from_object('config')
api = Api(app)


api.add_resource(Ping, '/v1/ping')
