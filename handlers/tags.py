import logging

import flask

from google.appengine.api import users

import models
import form_models

import repositories

def list(tag_name):

	user = users.get_current_user()

	all_tagged_posts = repositories.posts.all_posts_for_tag(user.user_id(), tag_name)

	template_values = {
		"tag_name": tag_name,
		"posts": all_tagged_posts
	}
	
	return flask.render_template('tags/list.html', **template_values)