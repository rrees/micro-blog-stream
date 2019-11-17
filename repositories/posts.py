from google.appengine.ext import ndb

from google.appengine.api import search

import models


posts_index = search.Index(name="posts")

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

def all_posts_for_tag(user_id, tag_name):
	query = models.Post.query(models.Post.tags.IN([tag_name])).order(-models.Post.updated_datetime)

	query.filter(ndb.OR(models.Post.private == False, models.Post.user_id == user_id))

	return query

def delete_post(post_id):
	post = read_post(post_id)
	post.key.delete()

	return post

def search(search_term):
	posts_index.search(search_term)
	return []

def all(user_id):
	query = models.Post.filter(models.Post.user_id == user_id)

	return query
