from src.utils.logger import Logger

def test_logger_info(capsys):
	logger = Logger()

	logger.info("System initialized")

	captured = capsys.readouterr()

	assert captured.out == "[INFO] System initialized\n"

def test_logger_warning(capsys):
	logger = Logger()

	logger.warning("Test warning")

	captured = capsys.readouterr()

	assert captured.out == "[WARNING] Test warning\n"
	
def test_logger_error(capsys):
	logger = Logger()

	logger.error("Test error")

	captured = capsys.readouterr()

	assert captured.out == "[ERROR] Test error\n"
