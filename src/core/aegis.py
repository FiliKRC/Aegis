from src.config import APP_NAME, VERSION, DEFAULT_MODEL, OLLAMA_BASE_URL
from src.utils.logger import Logger
from src.llm.ollama_client import OllamaClient

class Aegis:
	def __init__(self):
		self.name = APP_NAME
		self.version = VERSION
		self.model = DEFAULT_MODEL		
		self.status = "initialized"
		self.logger = Logger()
		self.client = OllamaClient(OLLAMA_BASE_URL)

		self.logger.info("Core loaded.")
		print(f"Version: {self.version}")
		print(f"Model: {self.model}")
		print(f"Status: {self.status}")

	def start(self):
		if self.status == 'running':
			self.logger.warning("Aegis is already running.")
		else:
			self.status = "running"
			self.logger.info("Aegis started.")
			print(f"Status: {self.status}")

	def ask(self, prompt):
		result = self.client.generate(prompt, self.model)
		return result

	def stop(self):
		if self.status == 'running':
			self.status = "stopped"
			self.logger.info("Aegis stopped.")
			print(f"Status: {self.status}")
		else:
			self.logger.warning("Aegis is already stopped.")
