import ckanapi
import os
from api.auth.auth import auth
from flask_restful import Resource, reqparse

HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)


class CreateOrganization(Resource):
    decorators=[auth.login_required]
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('org_name', type=str, required=True)
        query = parser.parse_args()
        existing_orgs = remote.action.organization_list()
        #if query['org_name'] not in existing_orgs:
        try:
            remote.action.organization_create(name=query['org_name'])
            return {'Organization created': query['org_name']}
        except ckanapi.ValidationError as e:
            if str(e) == "{u'__type': u'Validation Error', u'name': [u'Group name already exists in database']}":
                return {'Validation Error': 'Organization already exists'}
            else:
                return {'Error': 'Something went wrong'}
