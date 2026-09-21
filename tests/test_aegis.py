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

	agent.client.generate = Mock(return_value = "Risposta finta")

	result = agent.ask("Ciao")
	assert result == "Risposta finta"

	agent.client.generate.assert_called_once_with("Ciao", agent.model)

def test_stop_state():
	agent = Aegis()

	agent.start()

	agent.stop()

	assert agent.status == 'stopped'
