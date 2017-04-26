import logging
import os

import flask

import handlers
import filters

app = flask.Flask(__name__)

app.secret_key = os.urandom(24)

app.jinja_env.filters['safe_html'] = filters.safe_html

routes = [
	('/', 'index', handlers.front_page, ['GET', 'POST']),
	('/posts/new', 'new_post', handlers.posts.new, ['GET']),
	('/posts/new/form', 'new_post_form', handlers.forms.new_post, ['POST']),
	('/post/<post_id>/edit', 'edit_post', handlers.posts.edit, ['GET']),
	('/post/<post_id>/edit/form', 'edit_post_form', handlers.forms.edit_post, ['POST']),
]

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
