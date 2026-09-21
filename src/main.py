from src.core.aegis import Aegis

def main():
	agent = Aegis()
	agent.start()

	while True:
		mex = input("Tu: ")

		if mex == "Exit" or mex == "exit":
			break

		response = agent.ask(mex)
		print("Aegis: ", response)

	agent.stop()

if __name__ == "__main__":
	main()
