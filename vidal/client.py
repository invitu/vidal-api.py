import requests

class VidalClient(object):

	def __init__(self, api_key, server_url = "http://api.vidal.fr/"):
		self.api_key = api_key
		self.server_url = server_url

	def is_authenticated(self):
		"""
		Checks if we can contact server and the API Key is correct
		"""
		return requests.get(self.server_url).status_code == 200