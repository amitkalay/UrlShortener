from mongoengine import *
from datetime import datetime


class SimpleDataModel(Document):
    name = StringField(max_length=200, required=True)
    date_created  = DateTimeField(default=datetime.utcnow)
    num = IntField()
    meta = {'collection': 'all_urls'}
