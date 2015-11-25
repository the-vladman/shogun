from flask_restful import Resource, reqparse


def xstr(s):
    return '' if s is None else str(s)


class Organization(Resource):
    def exists_in_remote(self, name):
        return True


    # Updates metadata for an organization
    # See http://docs.ckan.org/en/latest/api/
    # index.html#ckan.logic.action.update.organization_update
    def put(self, name):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name')
        parser.add_argument('title')
        parser.add_argument('description')
        query = parser.parse_args()

        # Default to RESTful parameter
        organization_name = name
        if not (query['name'] is None):
            organization_name = query['name']

        if self.exists_in_remote(name=name):
            return {'organization': {
                    'name'          : organization_name,
                    'title'         : xstr(query['title']),
                    'description'   : xstr(query['description'])
                }}
        else:
            return {"message": "Organization not found in remote host"}


