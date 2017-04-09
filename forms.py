from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class NewPostForm(FlaskForm):
	title = StringField('title')
	content = TextAreaField('content', validators=[DataRequired()])
	tags = StringField('tags', validators=[DataRequired()])
