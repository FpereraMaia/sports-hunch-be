local-requirements:
	pip install -r local-requirements.txt

install-pre-commit:
	pre-commit install

setup-local-environment: local-requirements install-pre-commit

lint:
	pre-commit run --all-files

up-local-database:
	docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=sports_hunch -e MYSQL_USER=admin -e MYSQL_PASSWORD=1234 mysql:latest

migrate:
	python sports_hunch/manage.py migrate

seed:
	python sports_hunch/manage.py loaddata sports_hunch/initial_data.json
