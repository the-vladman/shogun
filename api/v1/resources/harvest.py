import os
from flask import jsonify
from flask_restful import Resource, reqparse
import ckanapi
from ckanops import dcat_to_utf8_dict, munge, converters, upsert_dataset

HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)


class Harvest(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('url', type=str, required=True)
        arg_url = parser.parse_args()
        catalog = dcat_to_utf8_dict(arg_url['url'])
        for dcat_dataset in catalog.get('dataset', []):
            ckan_dataset = converters.dcat_to_ckan(dcat_dataset)
            ckan_dataset['name'] = munge.munge_title_to_name(ckan_dataset['title'])
            ckan_dataset['state'] = 'active'
            new_dataset = upsert_dataset(remote, ckan_dataset)
        return jsonify({'harvest': 'executed'})
