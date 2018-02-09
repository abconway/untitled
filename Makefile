.PHONY: all test

all: clean venv setup seed run

install:
	npm install
	venv/bin/pip install -r requirements.txt

clean: delete-db
	rm -rf node_modules
	rm -rf venv

delete-db:
	rm -f db.sqlite3

recreate-db: delete-db
	venv/bin/python manage.py migrate

run:
	venv/bin/honcho start

seed:
	venv/bin/python manage.py loaddata user_data
	venv/bin/python manage.py loaddata title_data

setup: install recreate-db

test-django:
	@echo '============= Running Django Tests... ============='
	venv/bin/python manage.py test
	@echo '============== Django Tests Complete =============='

test-vue:
	@echo '=============== Running Vue Tests... =============='
	npm run test
	@echo '================ Vue Tests Complete ==============='

test: test-django test-vue

venv:
	virtualenv venv -p $(shell which python3)
