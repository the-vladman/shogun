import os
from flask_restful import Resource, reqparse
import ckanapi

HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)

class UpdateOrg(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('old-org-name', type=str, required=True)
        parser.add_argument('new-org-name', type=str, required=True)
        query = parser.parse_args()
        data = { 'name': query['new-org-name'], 'id':query['old-org-name'] }
        try:
            remote.call_action('organization_update', data)
            return {'Organization Updated': query['new-org-name']}
        except ckanapi.ValidationError as e:
            if str(e) == "{u'__type': u'Validation Error', u'name': [u'Group name already exists in database']}":
                return {'Validation Error': 'Organization already exists'}
            else:
                return {'Error': 'Something went wrong'}
