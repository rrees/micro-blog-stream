import models

def create_from_form(form):
	new_post = models.Post()


	form.populate_obj(new_post)

	new_post.put()
	return new_post

def recent():
	return models.Post.query()