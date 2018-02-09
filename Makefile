.PHONY: all test

all: venv setup run

install:
	npm install
	pip install -r requirements.txt

delete-db:
	rm -f db.sqlite3

recreate-db: delete-db
	./manage.py migrate

run:
	honcho start

setup: install recreate-db

test:
	@echo '============= Running Django Tests... ============='
	./manage.py test
	@echo '============== Django Tests Complete =============='
	@echo '=============== Running Vue Tests... =============='
	npm run test
	@echo '================ Vue Tests Complete ==============='

venv:
	rm -rf venv
	virtualenv venv -p $(which python3)
