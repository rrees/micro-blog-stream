import logging
import os

import flask

from google.appengine.api import users

import forms

from repositories import posts

app = flask.Flask(__name__)

app.secret_key = os.urandom(24)

def front_page():
    if flask.request.method == 'GET':
    	form = forms.NewPostForm()
    	
    	user = users.get_current_user()

    	recent_posts = posts.recent(user=user)

        return flask.render_template('index.html', form=form, recent_posts=recent_posts, user=user)

    form = forms.NewPostForm()
    if form.validate_on_submit():
    	logging.info('Valid form')
    	new_post = posts.create_from_form(form)
    	logging.info(new_post)
    return flask.redirect('/')