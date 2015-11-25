from flask_restful import Resource, reqparse


class Organization(Resource):
    # Updates metadata for an organization
    # See http://docs.ckan.org/en/latest/api/
    # index.html#ckan.logic.action.update.organization_update
    def put(self, name):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name')
        parser.add_argument('title')
        parser.add_argument('description')
        query = parser.parse_args()
        return {'organization': {
                'name'          : query['name'],
                'title'         : query['title'],
                'description'   : query['description']
            }}


