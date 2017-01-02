import logging
import os

import flask

import forms

app = flask.Flask(__name__)

app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def front_page():
    if flask.request.method == 'GET':
    	form = forms.NewStreamForm()
        return flask.render_template('index.html', form=form)
    return flask.redirect('/')

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
