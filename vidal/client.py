import requests
from urllib.parse import urlencode

class QueryPart:

    def __init__(self, client, url_part):
        self.client = client
        self.url_part = url_part

    def get(self, **kwargs):
        url = "".join([self.url_part, "?", urlencode(kwargs)]) if kwargs else self.url_part
        return self.client._get(url)
    
    def __call__(self, name):
        return self._createPath(name)
    
    def __getattr__(self, name):
        return self._createPath(name)

    def _createPath(self, arg):
        return QueryPart(self.client, "/".join([self.url_part, str(arg)]))


class VidalClient:
    REST_PREFIX = "rest/api"

    def __init__(self, api_key, server_url = "http://api.vidal.fr"):
        self.api_key = api_key
        self.server_url = server_url

    def is_authenticated(self):
        """
        Checks if we can contact server and the API Key is correct
        """
        return requests.get(self.server_url).status_code == 200

    def _get(self, url):
        print(url)
        return requests.get(url)

    def __getattr__(self, name):
        return QueryPart(self, "/".join([self.server_url, VidalClient.REST_PREFIX, str(name)]))