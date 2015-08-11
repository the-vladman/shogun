from flask.ext.testing import TestCase
from api.app import app


class PingTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def test_ping(self):
        response = self.client.get('/v1/ping')
        self.assertEqual(response.json, {'ping': 'pong'})
