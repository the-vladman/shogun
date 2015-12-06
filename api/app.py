import logging

from api.auth.users import app
from api.v1.resources.createorganization import CreateOrganization
from api.v1.resources.finddatasets import FindDatasets
from api.v1.resources.harvest import Harvest
from api.v1.resources.ping import Ping,PingAuth
from api.v1.resources.tokens import Token
from flask_restful import Api

#Config in bare_app.py

api = Api(app=app)
api.add_resource(Token, '/token')
api.add_resource(Ping, '/v1/ping')
api.add_resource(PingAuth, '/v1/ping_auth')
api.add_resource(FindDatasets, '/v1/finddataset')
api.add_resource(CreateOrganization, '/v1/createorg')
api.add_resource(Harvest, '/v1/harvest')


handler = logging.StreamHandler()
handler.setLevel(app.config['LEVEL'])
app.logger.addHandler(handler)
