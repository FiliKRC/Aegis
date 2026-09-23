from src.config import APP_NAME, VERSION, DEFAULT_MODEL, OLLAMA_BASE_URL
from src.prompts.builder import build_normal_prompt, build_red_prompt
from src.utils.logger import Logger
from src.llm.ollama_client import OllamaClient
from urllib.error import URLError

class Aegis:
	def __init__(self, mode = "normal", red_module = None):
		self.name = APP_NAME
		self.version = VERSION
		self.model = DEFAULT_MODEL		
		self.status = "initialized"
		self.logger = Logger()
		self.client = OllamaClient(OLLAMA_BASE_URL)

		if mode == "red-team":
			self.system_prompt = build_red_prompt(red_module)

		else:
			self.system_prompt = build_normal_prompt()
		
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

		try:
			result = self.client.chat(self.history, self.model)

		except URLError:
			self.history.pop()
			self.logger.error("Ollama non disponibile.")
			return "Non riesco a collegarmi a Ollama."

		self.history.append({"role": "assistant", "content": result})
		return result

	def stop(self):
		if self.status == 'running':
			self.status = "stopped"
			self.logger.info("Aegis stopped.")
			print(f"Status: {self.status}")
		else:
			self.logger.warning("Aegis is already stopped.")
