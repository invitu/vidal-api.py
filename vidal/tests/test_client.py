import unittest
import responses

from vidal import client

class AuthentificationTest(unittest.TestCase):

    def setUp(self):
        self.client = client.VidalClient(api_key = "")

    @responses.activate
    def test_auth_forbidden(self):
        responses.add(responses.GET, 'http://api.vidal.fr', status=403)

        self.assertFalse(self.client.is_authenticated())

    @responses.activate
    def test_auth_all_good(self):
        responses.add(responses.GET, 'http://api.vidal.fr', status=200)

        self.assertTrue(self.client.is_authenticated())

    @responses.activate
    def test_auth_when_internal_server_error(self):
        responses.add(responses.GET, 'http://api.vidal.fr', status=500)

        self.assertFalse(self.client.is_authenticated())

if __name__ == '__main__':
    unittest.main()