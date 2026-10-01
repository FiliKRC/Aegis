from unittest.mock import patch, Mock
from src.llm.ollama_client import OllamaClient
from urllib.error import URLError

def test_ollama_available():

	response = Mock()
	response.status = 200

	with patch("src.llm.ollama_client.urlopen") as mock_urlopen:
		mock_urlopen.return_value = response

		client = OllamaClient("http://localhost:11434")

		assert client.is_available() is True


def test_ollama_unavailable():
	
	with patch("src.llm.ollama_client.urlopen") as mock_urlopen:
		mock_urlopen.side_effect = URLError("Connection refused")

		client = OllamaClient("http://localhost:11434")

		assert client.is_available() is False	


def test_list_models():

	response = Mock()

	response.read.return_value = b'{"models": [{"name": "qwen3:4b"},{"name": "llama3:8b"}]}'

	with patch("src.llm.ollama_client.urlopen") as mock_urlopen:
		mock_urlopen.return_value = response

		client = OllamaClient("http://localhost:11434")

		assert client.list_models() == ["qwen3:4b","llama3:8b"]


def test_generate():
	response = Mock()
	response.read.return_value = b'{"response": "Ciao da Aegis"}'

	with patch("src.llm.ollama_client.urlopen") as mock_urlopen:
		mock_urlopen.return_value = response
	
		client = OllamaClient("http://localhost:11434")

		assert client.generate("Ciao", "qwen3:4b") == "Ciao da Aegis"


def test_chat():
	response = Mock()
	response.read.return_value = b'{"message": {"content": "Ciao"}}'

	with patch("src.llm.ollama_client.urlopen") as mock_urlopen:
		mock_urlopen.return_value = response

		client = OllamaClient("http://localhost:11434")

		messages = [{"role": "user", "content": "Ciao"}]

		result = client.chat(messages, "qwen3:4b")

		assert result == "Ciao"