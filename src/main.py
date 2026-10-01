from src.core.aegis import Aegis
import sys

def main():
	mode = sys.argv[1] if len(sys.argv) > 1 else "normal"
	red_module = sys.argv[2] if len(sys.argv) > 2 else None

	if mode not in ["normal", "red-team"]:
		print("Modalità non valida. Usa: normal oppure red-team")
		return

	try:
		agent = Aegis(mode, red_module)

	except ValueError as error:
		print(error)
		return
	
	agent.start()

	try:
		while True:
			mex = input("Tu: ")

			if mex == "Exit" or mex == "exit":
				break

			response = agent.ask(mex)
			print("Aegis: ", response)
			
	except KeyboardInterrupt:
		print()

	finally:
		agent.stop()

if __name__ == "__main__":
	main()
