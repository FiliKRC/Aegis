from src.core.aegis import Aegis
from unittest.mock import Mock
from urllib.error import URLError

def test_initial_state():
	agent = Aegis() 
	
	assert agent.status == 'initialized'

def test_start_state():
	agent = Aegis()

	agent.start()

	assert agent.status == 'running'

def test_ask():
    agent = Aegis()

    agent.client.chat = Mock(return_value="Risposta finta")

    result = agent.ask("Ciao")

    assert result == "Risposta finta"

    assert agent.history[-2] == {
        "role": "user",
        "content": "Ciao"
    }

    assert agent.history[-1] == {
        "role": "assistant",
        "content": "Risposta finta"
    }

    agent.client.chat.assert_called_once()
	
def test_ask_ollama_unavailable():
    agent = Aegis()

    agent.client.chat = Mock(
        side_effect=URLError("Connection refused")
    )

    result = agent.ask("Ciao")

    assert result == "Non riesco a collegarmi a Ollama."

    assert len(agent.history) == 1

def test_stop_state():
	agent = Aegis()

	agent.start()

	agent.stop()

	assert agent.status == 'stopped'
