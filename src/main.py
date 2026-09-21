from src.core.aegis import Aegis
import sys

def main():
	mode = sys.argv[1] if len(sys.argv) > 1 else "normal"

	if mode not in ["normal", "red-team"]:
		print("Modalità non valida. Usa: normal oppure red-team")
		return

	agent = Aegis(mode)
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
