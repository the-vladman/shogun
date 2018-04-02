import os
from flask_restful import Resource, reqparse
import ckanapi

HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)

class UpdateOrg(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('old_org_name', type=str, required=True)
        parser.add_argument('new_org_name', type=str, required=True)
        query = parser.parse_args()
        try:
            remote.action.organization_update(id=query['old_org_name'], name=query['new_org_name'])
            return {'Organization Updated': query['new_org_name']}
        except ckanapi.ValidationError as e:
            if str(e) == "{u'__type': u'Validation Error', u'name': [u'Group name already exists in database']}":
                return {'Validation Error': 'Organization already exists'}
            else:
                return {'Error': 'Something went wrong'}
