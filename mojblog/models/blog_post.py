import datetime
from peewee import DateTimeField, ForeignKeyField, TextField, BooleanField
from freenit.db import db
from .user import User

Model = db.Model

class BlogPost(Model):
    slug = TextField()
    title = TextField()
    content = TextField()
    date = DateTimeField(
        default=datetime.datetime.utcnow
    )
    author = ForeignKeyField(User, backref='blogpost')
    published = BooleanField()
