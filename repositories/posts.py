import models

def create_from_form(form):
	new_post = models.Post()


	form.populate_obj(new_post)

	new_post.put()
	return new_post

def recent(user = None):
	if not user:
		return models.Post.query()

	return models.Post.query().filter(models.Post.user_id == user.user_id())