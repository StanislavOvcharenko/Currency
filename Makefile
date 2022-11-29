SHELL := /bin/bash

manage_py := docker exec -it backend python app/manage.py

run:
	python3 app/manage.py runserver

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

build_and_run: makemigrations \
	migrate \
	run

shell:
	$(manage_py) shell_plus --print-sql


celery:
	cd app && celery -A settings worker --loglevel=INFO

celerybeat:
	cd app && celery -A settings beat --loglevel=INFO

pytest:
	pytest app/tests/


coverage:
	pytest --cov=app app/tests/ --cov-report html && coverage report --fail-under=79.0000

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"

gunicorn:
	cd app && gunicorn settings.wsgi:application --bind 0.0.0.0:8001 --workers 10 --threads 4 --log-level info --max-requests 1000 --timeout 10

uwsgi:
	cd app && uwsgi --http-socket 0.0.0.0:8001 --module settings.wsgi --threads 2 --workers 4 --logto /tmp/mylog.log