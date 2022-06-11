local-requirements:
	pip install -r local-requirements.txt

install-pre-commit:
	pre-commit install

setup-local-environment: local-requirements install-pre-commit

lint:
	pre-commit run --all-files