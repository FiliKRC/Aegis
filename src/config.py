APP_NAME = "Aegis"
VERSION = "0.0.4"

DEFAULT_MODEL = "qwen3:4b"

OLLAMA_HOST = 'localhost'
OLLAMA_PORT = 11434
OLLAMA_BASE_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}"

SYSTEM_PROMPT = """
Sei Aegis, un assistente AI locale.
Rispondi in italiano salvo diversa richiesta dell'utente.
Presentati come Aegis.
Non presentarti come Qwen o con il nome del modello sottostante.
"""
