from flask_wtf import FlaskForm
from wtforms import Field, StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

import custom_fields

class NewPostForm(FlaskForm):
	title = StringField('title')
	content = TextAreaField('content', validators=[DataRequired()])
	private = BooleanField('private')
	tags = custom_fields.TagListField('tags', validators=[DataRequired()])
	user_id = StringField('user_id', validators=[DataRequired()])

class DeletePostForm(FlaskForm):
	post_id = StringField('post_id', validators=[DataRequired()])

class SearchForm(FlaskForm):
	search_term = StringField('search_term', validators=[DataRequired()])