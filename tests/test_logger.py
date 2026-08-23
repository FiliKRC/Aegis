from src.utils.logger import Logger

def test_logger_info(capsys):
	logger = Logger()

	logger.info("System initialized")

	captured = capsys.readouterr()

	assert captured.out == "[INFO] System initialized\n"
