from flask_restful import Resource, reqparse

class Organization(Resource):
    def put(self, organization_id):
        return {organization_id: 'updated'}


