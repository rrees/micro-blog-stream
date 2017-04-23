from google.appengine.ext import ndb

import models

def create_from_form(form):
	new_post = models.Post()


	form.populate_obj(new_post)

	new_post.put()
	return new_post

def recent(user = None, include_private=False):
	query = models.Post.query().order(-models.Post.updated_datetime)

	if not user:
		return query.filter(models.Post.private == False)
		
	return query.filter(models.Post.user_id == user.user_id())

def read_post(post_id):

	key = ndb.Key(urlsafe=post_id)

	return key.get()

def update_from_form(post_id, form):
	post = read_post(post_id)

	form.populate_obj(post)

	post.put()
	return post