from urllib.request import urlopen, Request
from urllib.error import URLError
import json

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
		

	def list_models(self):
		url = f"{self.base_url}/api/tags"
		
		response = urlopen(url)
		data = json.loads(response.read())

		models = []
		
		for model in data["models"]:
			models.append(model["name"])
			
		return models


	def generate(self, prompt, model):
		url = f"{self.base_url}/api/generate"
				
		payload = {"model": model, "prompt": prompt, "stream": False}

		data = json.dumps(payload)
		data = data.encode("utf-8")

		request = Request(url, data = data, method = "POST", headers = {"Content-Type": "application/json"})
		response = urlopen(request)
		result = json.loads(response.read())

		return result["response"]