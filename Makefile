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
	./manage.py test
	npm run test

venv:
	rm -rf venv
	virtualenv venv -p $(which python3)