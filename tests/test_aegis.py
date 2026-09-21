from src.core.aegis import Aegis
from unittest.mock import Mock

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

def test_stop_state():
	agent = Aegis()

	agent.start()

	agent.stop()

	assert agent.status == 'stopped'
