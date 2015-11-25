from flask.ext.testing import TestCase
from api.app import app


class PingTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app


    def test_ping(self):
        response = self.client.get('/v1/ping')
        self.assertEqual(response.json, {'ping': 'pong'})


class OrganizationTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app


    def test_update_returns_organization_with_new_values(self):
        attributes = dict(
            name='fubar',
            title='Foo Inc.',
            description='Beyond recognition'
        )
        expected = {u'organization': attributes}
        response = self.client.put('/v1/organization/fubar', data=attributes)
        self.assertEqual(response.json, expected)


    def test_grabs_name_from_rest_parameter_as_default(self):
        expected = {
            u'organization': {
                u'name'         : u'fubar',
                u'title'        : u'',
                u'description'  : u''
            }
        }
        response = self.client.put('/v1/organization/fubar')
        self.assertEqual(response.json, expected)


