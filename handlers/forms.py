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

def edit_post(post_id):
    form = form_models.NewPostForm()
    if form.validate_on_submit():
    	logging.info('Valid form')
    	new_post = posts.update_from_form(post_id, form)
    	logging.info(new_post)
    return flask.redirect('/')


def delete_post(post_id):
    form = form_models.DeletePostForm()
    if form.validate_on_submit():
        post_id = form.data.get('post_id')
        post = posts.delete_post(post_id)
    return flask.redirect('/')