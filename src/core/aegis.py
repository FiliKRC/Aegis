from src.config import APP_NAME, VERSION, DEFAULT_MODEL

class Aegis:
	def __init__(self):
		self.name = APP_NAME
		self.version = VERSION
		self.model = DEFAULT_MODEL		
		self.status = "initialized"

		print(f"{self.name} core loaded.")
		print(f"Version: {self.version}")
		print(f"Model: {self.model}")
		print(f"Status: {self.status}")

	def start(self):
		if self.status == 'running':
			print("Aegis is already running.")
		else:
			self.status = "running"
			print("Aegis started.")
			print(f"Status: {self.status}")

	def stop(self):
		if self.status == 'running':
			self.status = "stopped"
			print("Aegis stopped.")
			print(f"Status: {self.status}")
		else:
			print("Aegis is already stopped.")
