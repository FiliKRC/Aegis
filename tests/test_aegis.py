from src.core.aegis import Aegis

def test_initial_state():
	agent = Aegis() 
	
	assert agent.status == 'initialized'

