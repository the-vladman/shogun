from api.auth.auth import auth
from flask_restful import Resource


class Ping(Resource):
    def get(self):
        return {'ping': 'pong'}

class PingAuth(Resource):
    decorators=[auth.login_required]
    def get(self):
        return {u'chin': u'champu'}
