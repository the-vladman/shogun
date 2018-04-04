import os
from flask_restful import Resource, reqparse
import ckanapi

HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)

class UpdateOrg(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('oldname', type=str, location='args')
        parser.add_argument('newname', type=str, location='args')
        query = parser.parse_args()
        data = { 'name': "newname", 'id':query['oldname'] }
        return data
