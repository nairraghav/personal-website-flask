lint:
	flake8 app/ tests/

format:
	black app/ --line-length 79
