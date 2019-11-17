import logging
import os

import flask

from google.appengine.api import users

import form_models
import models

from repositories import posts

def front_page():
	form = form_models.NewPostForm()

	user = users.get_current_user()

	recent_posts = posts.recent(user=user)

	return flask.render_template('index.html', form=form, recent_posts=recent_posts, user=user)

def export():
	user = users.get_current_user()

	all_posts = posts.recent(user=user)

	post_data = [models.post_to_dict(post) for post in all_posts]

	return flask.jsonify(post_data)