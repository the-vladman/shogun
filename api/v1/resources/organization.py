# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse


class Organization(Resource):
    # Updates metadata for an organization
    # See http://docs.ckan.org/en/latest/api/
    # index.html#ckan.logic.action.update.organization_update
    def put(self, name):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name', type=str)
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        query = parser.parse_args()
        return {'organization': {
                u'name'          : unicode(query['name']),
                u'title'         : unicode(query['title']),
                u'description'   : unicode(query['description'])
            }}


