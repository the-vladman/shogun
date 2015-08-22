from flask import Flask
from flask_restful import Api
from api.v1.resources.ping import Ping
from api.v1.resources.finddatasets import FindDatasets

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

api.add_resource(Ping, '/v1/ping')
api.add_resource(FindDatasets, '/v1/finddataset/<string:query>')
