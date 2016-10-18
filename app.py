import logging

import flask

import forms

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def front_page():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')
    return flask.redirect('/')

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
