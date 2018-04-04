import os
from flask_restful import Resource, reqparse
import ckanapi

HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)

class UpdateOrg(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('oldname', type=str, required=True)
        parser.add_argument('newname', type=str, required=True)
        query = parser.parse_args()
        data = { 'name': query['newname'], 'id':query['oldname'] }
        try:
            remote.call_action('organization_update', data)
            return jsonify({'Organization Updated': query['newname']})
        except ckanapi.ValidationError as e:
            if str(e) == "{u'__type': u'Validation Error', u'name': [u'Group name already exists in database']}":
                return jsonify({'Validation Error': 'Organization already exists'})
            else:
                return jsonify({'Error': 'Something went wrong'})
