from google.appengine.ext import ndb

class Post(ndb.Model):
	content = ndb.TextProperty(required=True)
	title = ndb.StringProperty()
	tags = ndb.StringProperty(repeated=True)
	created_datetime = ndb.DateTimeProperty(auto_now_add = True)
	updated_datetime = ndb.DateTimeProperty(auto_now = True)
