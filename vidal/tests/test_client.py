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


class ChainedCommandTest(unittest.TestCase):

    def setUp(self):
        self.client = client.VidalClient(api_key = "")

    @responses.activate
    def test_chained_command_get(self):
        responses.add(responses.GET, 'http://api.vidal.fr/rest/api/product/94930/packages', status=200)

        result = self.client.product(94930).packages.get()
        self.assertTrue(result is not None)



if __name__ == '__main__':
    unittest.main()