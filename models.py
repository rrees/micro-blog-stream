from google.appengine.ext import ndb

class Post(ndb.Model):
	content = ndb.TextProperty(required=True)
	title = ndb.StringProperty()
	tags = ndb.StringProperty(repeated=True)
	private = ndb.BooleanProperty(required=True, default=False)
	user_id = ndb.StringProperty(required=True)
	created_datetime = ndb.DateTimeProperty(auto_now_add = True)
	updated_datetime = ndb.DateTimeProperty(auto_now = True)
