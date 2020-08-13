install:
	pipenv install
run:
	FLASK_APP=server.py FLASK_ENV=development pipenv run flask run
run_prod:
	pipenv run gunicorn wsgi:app