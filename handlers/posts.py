
import flask

from google.appengine.api import users

import form_models

def new():
	form = form_models.NewPostForm()

	user = users.get_current_user()

	return flask.render_template('posts/new.html', form=form, user=user)