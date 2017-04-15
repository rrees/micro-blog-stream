
import flask

from google.appengine.api import users

import forms

def new():
	form = forms.NewPostForm()

	user = users.get_current_user()

	recent_posts = []

	return flask.render_template('index.html', form=form, recent_posts=recent_posts, user=user)