from mongoengine import *
from datetime import datetime


class UrlInfo(Document):
    short_url = StringField(max_length=20, required=True)
    long_url = StringField(max_length=300, required=True)
    date_accessed = DateTimeField(default=datetime.utcnow)
    meta = {'collection': 'all_urls'}