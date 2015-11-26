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
db.create_all()
auth = HTTPBasicAuth()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(64))

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.title

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self):
        s = Serializer(app.config['SECRET_KEY'])
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user


passwd=app.config['PASSWORD']
username=app.config['USER']

user = User(username=username)
user.hash_password(passwd)
db.session.add(user)


class Token(Resource):
    def __init__(self):
        super(Token, self).__init__()

    def get(self):
        g.user = user
        token = g.user.generate_auth_token()
        return {'token': token.decode('ascii')}


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

api = Api(app=app)
api.add_resource(Token, '/token')


api = Api(app=app,decorators=[auth.login_required])


api.add_resource(Ping, '/v1/ping')
#api.add_resource(FindDatasets, '/v1/finddataset')
#api.add_resource(CreateOrganization, '/v1/createorg')
#api.add_resource(Harvest, '/v1/harvest')


handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
