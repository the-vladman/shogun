import os
from flask_restful import Resource, reqparse
import ckanapi
from ckanops import find_datasets_with_query

HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)


class FindDatasets(Resource):
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('title', type=str, required=True)
        query = parser.parse_args()
        ds = find_datasets_with_query(remote, query)
        for d in ds[u'results']:
            return {'title': d['title']}
