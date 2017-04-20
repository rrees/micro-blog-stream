from google.appengine.ext import ndb

import models

def create_from_form(form):
	new_post = models.Post()


	form.populate_obj(new_post)

	new_post.put()
	return new_post

def recent(user = None, include_private=False):
	if not user:
		return models.Post.query().filter(models.Post.private == False)

	return models.Post.query().filter(models.Post.user_id == user.user_id())

def post(post_id):

	key = ndb.Key(urlsafe=post_id)

	return key.get()