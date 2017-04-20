import logging

import flask

from google.appengine.api import users

import form_models

import repositories

def new():
	form = form_models.NewPostForm()

	user = users.get_current_user()

	return flask.render_template('posts/new.html', form=form, user=user)

def edit(post_id):

	user = users.get_current_user()

	post = repositories.posts.post(post_id)
	logging.info(post)

	form = form_models.NewPostForm()

	return flask.render_template('posts/new.html', form=form, user=user)