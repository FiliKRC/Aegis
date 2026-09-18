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
