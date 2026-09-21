from src.config import APP_NAME, VERSION, DEFAULT_MODEL, OLLAMA_BASE_URL, SYSTEM_PROMPT
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
		self.system_prompt = SYSTEM_PROMPT
		self.history = [{"role": "system", "content": self.system_prompt}]

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
		self.history.append({"role": "user", "content": prompt})
		result = self.client.chat(self.history, self.model)

		self.history.append({"role": "assistant", "content": result})
		return result

	def stop(self):
		if self.status == 'running':
			self.status = "stopped"
			self.logger.info("Aegis stopped.")
			print(f"Status: {self.status}")
		else:
			self.logger.warning("Aegis is already stopped.")
