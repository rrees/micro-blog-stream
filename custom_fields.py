import wtforms

import tags

class TagListField(wtforms.Field):
    widget = wtforms.widgets.TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = tags.extract_tags(valuelist[0])
        else:
            self.data = []