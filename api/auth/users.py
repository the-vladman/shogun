from flask.ext.sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from api.bare_app import app
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(64))

    def __init__(self,username,config):
        self.username = username
        self.config = config

    def __repr__(self):
        return '<User %r>' % self.title

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self):
        s = Serializer('garlic')
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY']) #config0['SECRET_KEY']
        try:
            data = s.loads(token)
        except SignatureExpired:
            app.logger.warn('Expired Token: ' + token)
            return None
        except BadSignature:
            app.logger.warn('Unauthorized Token: ' + token)
            return None
        user = User.query.get(data['id'])
        app.logger.info('User ' +  user.username + ' Authenticated')
        return user
