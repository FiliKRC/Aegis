from config import APP_NAME, VERSION, DEFAULT_MODEL

class Aegis:
	def __init__(self):
		self.name = APP_NAME
		self.version = VERSION
		self.model = DEFAULT_MODEL		

		print(f"{self.name} core loaded.")
		print(f"Version: {self.version}")
		print(f"Model: {self.model}")

	def start(self):
		print("Aegis started.")
