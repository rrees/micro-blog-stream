from flask_wtf import FlaskForm
from wtforms import Field, StringField, TextAreaField
from wtforms.widgets import TextInput
from wtforms.validators import DataRequired

class TagListField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.lower().strip() for x in valuelist[0].split(',')]
        else:
            self.data = []

class NewPostForm(FlaskForm):
	title = StringField('title')
	content = TextAreaField('content', validators=[DataRequired()])
	tags = TagListField('tags', validators=[DataRequired()])
