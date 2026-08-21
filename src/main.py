from core.aegis import Aegis

def main():
	agent = Aegis()
	agent.start()
	agent.start()
	agent.stop()
	agent.stop()

if __name__ == "__main__":
	main()
