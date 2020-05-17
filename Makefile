lint:
	flake8 app/

format:
	black app/ --line-length 79

install:
	pip install -r requirements.txt
