import logging
import os

import flask

import forms
import handlers

app = flask.Flask(__name__)

app.secret_key = os.urandom(24)

routes = [
	('/', 'index', handlers.front_page, ['GET', 'POST']),
]

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
