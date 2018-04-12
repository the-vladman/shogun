import os
from flask_restful import Resource, reqparse
import ckanapi
from flask import jsonify

HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)

class UpdateOrg(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('oldname', type=str, required=True)
        parser.add_argument('newname', type=str, required=True)
        parser.add_argument('newtitle', type=str, required=True)
        query = parser.parse_args()
        data = { 'name': query['newname'], 'id':query['oldname'], 'title': query['newtitle']}
        try:
            org = remote.call_action('organization_update', data)
            datasetsToUpdated = org['packages']
            for d in datasetsToUpdated:
                remote.action.package_owner_org_update(id= d['id'], organization_id = org['id'])
            return jsonify({'Organization Updated': query['newname']})

        except ckanapi.ValidationError as e:
            if str(e) == "{u'__type': u'Validation Error', u'name': [u'Group name already exists in database']}":
                return jsonify({'Validation Error': 'Organization already exists'})
            else:
                return jsonify({'Error': 'Something went wrong'})
