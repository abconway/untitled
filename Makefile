.PHONY: all test

all: venv setup seed run

install:
	npm install
	pip install -r requirements.txt

delete-db:
	rm -f db.sqlite3

recreate-db: delete-db
	./manage.py migrate

run:
	honcho start

seed:
	./manage.py loaddata user_data
	./manage.py loaddata title_data

setup: install recreate-db

test-django:
	@echo '============= Running Django Tests... ============='
	./manage.py test
	@echo '============== Django Tests Complete =============='

test-vue:
	@echo '=============== Running Vue Tests... =============='
	npm run test
	@echo '================ Vue Tests Complete ==============='

test: test-django test-vue

venv:
	rm -rf venv
	virtualenv venv -p $(which python3)
