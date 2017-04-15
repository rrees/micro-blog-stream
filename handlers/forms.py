import logging

import flask

import form_models
from repositories import posts

def new_post():
    form = form_models.NewPostForm()
    if form.validate_on_submit():
    	logging.info('Valid form')
    	new_post = posts.create_from_form(form)
    	logging.info(new_post)
    return flask.redirect('/')