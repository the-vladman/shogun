from api.auth.auth import auth
from flask_restful import Resource
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from api.auth.users import User,app


class Token(Resource):
    decorators=[auth.login_required]
    def __init__(self):
        super(Token, self).__init__()

    def get(self):
        username = app.config['USER']
        secret = app.config['SECRET_KEY']
        s = Serializer(secret)
        app.logger.info('User: '+ username )
        try:
            user = User.query.filter_by(username=username).first()
        except SignatureExpired:
            app.logger.warn('User: '+ username )
            app.logger.warn('Token Expired')
            return None
        except BadSignature:
            app.logger.warn('User: '+ username )
            app.logger.warn('Unauthorized')
            return None
        app.logger.info('Authenticated')
        return s.dumps({'id': user.id})
