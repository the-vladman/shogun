import os
import json
import urllib2
from urlparse import urlparse
from flask import jsonify
from flask_restful import Resource, reqparse
import ckanapi
from tasks import harvesting


HOST = os.getenv('CKAN_HOST')
TOKEN = os.getenv('CKAN_API_TOKEN')
CATALOG = os.getenv('CATALOG_HOST')

remote = ckanapi.RemoteCKAN(HOST, user_agent='ckanops/1.0', apikey=TOKEN)


class Harvest(Resource):
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
        harvesting.delay(arg_url['url'])
        return jsonify({'harvest': 'executed'})
