import logging
from flask import Flask, g
from flask_restful import Api, Resource, reqparse
from api.v1.resources.ping import Ping
from api.v1.resources.finddatasets import FindDatasets
from api.v1.resources.createorganization import CreateOrganization
from api.v1.resources.harvest import Harvest
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

app = Flask(__name__)
app.config.from_object('config.TestConfig')
db = SQLAlchemy(app)
from users import User


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    app.logger.debug(username_or_token)
    app.logger.debug(password)
    return True


api = Api(app=app,decorators=[auth.login_required])
api.add_resource(Ping, '/v1/ping')
api.add_resource(FindDatasets, '/v1/finddataset')
api.add_resource(CreateOrganization, '/v1/createorg')
api.add_resource(Harvest, '/v1/harvest')


handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)
