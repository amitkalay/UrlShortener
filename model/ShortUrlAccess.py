from mongoengine import *
from datetime import datetime


class ShortUrlAccess(Document):
    short_url = StringField(max_length=20, required=True)
    date_accessed = DateTimeField(default=datetime.utcnow)
    meta = {'collection': 'short_url_access'}