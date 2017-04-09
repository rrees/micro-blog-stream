import logging
import os

import flask

import forms

from repositories import posts

app = flask.Flask(__name__)

app.secret_key = os.urandom(24)

def front_page():
    if flask.request.method == 'GET':
    	form = forms.NewPostForm()
    	recent_posts = posts.recent()
        return flask.render_template('index.html', form=form, recent_posts=recent_posts)

    form = forms.NewPostForm()
    if form.validate_on_submit():
    	logging.info('Valid form')
    	new_post = posts.create_from_form(form)
    	logging.info(new_post)
    return flask.redirect('/')