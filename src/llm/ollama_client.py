from urllib.request import urlopen
from urllib.error import URLError

class OllamaClient:
	def __init__(self, base_url):
		self.base_url = base_url

	def is_available(self):
		url = f"{self.base_url}/api/tags"

		try:
			response = urlopen(url)
			return response.status == 200
		
		except URLError:
			return False
