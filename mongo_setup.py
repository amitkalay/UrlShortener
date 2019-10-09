from mongoengine import *


def global_init():
    connect('tinyurl_db')