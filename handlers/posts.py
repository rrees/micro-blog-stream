
import flask

from google.appengine.api import users

import forms

def new():
	form = forms.NewPostForm()

	user = users.get_current_user()

	return flask.render_template('posts/new.html', form=form, user=user)