import json
import urllib2
from urlparse import urlparse

import ckanapi
import os
from api.auth.auth import auth
from ckanops import dcat_to_utf8_dict, munge, converters, upsert_dataset
from flask import jsonify
from flask_restful import Resource, reqparse

HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')
CATALOG = os.getenv('CATALOG_HOST')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)


class Harvest(Resource):
    decorators=[auth.login_required]
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('url', type=str, required=True)
        arg_url = parser.parse_args()
        org_url = urlparse(arg_url['url'])
        org_name = org_url.path.split("/")[1]
        catalog_org = CATALOG + org_name
        opener = urllib2.build_opener()
        f = opener.open(catalog_org)
        j = json.load(f)
        try:
            remote.action.organization_create(name=org_name, title=j['title'], description=j['description'])
        except ckanapi.ValidationError:
            pass
        catalog = dcat_to_utf8_dict(arg_url['url'])
        for dcat_dataset in catalog.get('dataset', []):
            ckan_dataset = converters.dcat_to_ckan(dcat_dataset)
            ckan_dataset['name'] = munge.munge_title_to_name(ckan_dataset['title'])
            ckan_dataset['state'] = 'active'
            new_dataset = upsert_dataset(remote, ckan_dataset)
        return jsonify({'harvest': 'executed'})
