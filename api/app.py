import logging
from flask import Flask
from flask_restful import Api
from api.v1.resources.ping import Ping
from api.v1.resources.finddatasets import FindDatasets
from api.v1.resources.createorganization import CreateOrganization
from api.v1.resources.harvest import Harvest
from api.v1.resources.update_org import UpdateOrg

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

api.add_resource(Ping, '/v1/ping')
api.add_resource(FindDatasets, '/v1/finddataset')
api.add_resource(CreateOrganization, '/v1/createorg')
api.add_resource(UpdateOrg, '/v1/updateorg')
api.add_resource(Harvest, '/v1/harvest')

handler = logging.FileHandler(filename='shogun.log', mode='w')
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
