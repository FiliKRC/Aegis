from src.core.aegis import Aegis

def test_initial_state():
	agent = Aegis() 
	
	assert agent.status == 'initialized'

def test_start_state():
	agent = Aegis()

	agent.start()

	assert agent.status == 'running'

def test_stop_state():
	agent = Aegis()

	agent.start()

	agent.stop()

	assert agent.status == 'stopped'
