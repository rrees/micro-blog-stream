from flask_wtf import FlaskForm
from wtforms import Field, StringField, TextAreaField
from wtforms.validators import DataRequired

import custom_fields

class NewPostForm(FlaskForm):
	title = StringField('title')
	content = TextAreaField('content', validators=[DataRequired()])
	tags = custom_fields.TagListField('tags', validators=[DataRequired()])
	user_id = StringField('user_id', validators=[DataRequired()])
