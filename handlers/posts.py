import logging

import flask

from google.appengine.api import users

import models
import form_models

import repositories

def new():
	form = form_models.NewPostForm()

	user = users.get_current_user()

	return flask.render_template('posts/new.html', form=form, user=user)

def edit(post_id):

	user = users.get_current_user()

	post = repositories.posts.read_post(post_id)
	#logging.info(models.post_as_tuple(post))

	form = form_models.NewPostForm(obj=models.post_as_tuple(post))

	return flask.render_template('posts/edit.html', post=post, form=form, user=user)

def show(post_id):

	user = users.get_current_user()

	post = repositories.posts.read_post(post_id)

	if post.private and not post.user_id == user.user_id:
		abort(403)

	return flask.render_template('posts/show.html', post=post, user=user)