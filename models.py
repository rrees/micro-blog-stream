from google.appengine.ext import ndb

class Stream(ndb.Model):
	name = ndb.StringProperty(required=True)
	description = ndb.StringProperty()
	created_datetime = ndb.DateTimeProperty(auto_now_add = True)
	updated_datetime = ndb.DateTimeProperty(auto_now = True)

class Post(ndb.Model):
	content = ndb.TextProperty(required=True)
	title = ndb.StringProperty()
	tags = ndb.StringProperty(repeated=True)
	stream_key = ndb.KeyProperty(kind=Stream)
	created_datetime = ndb.DateTimeProperty(auto_now_add = True)
	updated_datetime = ndb.DateTimeProperty(auto_now = True)
