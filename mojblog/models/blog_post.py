import datetime
from freenit.db import db
from peewee import DateTimeField, ForeignKeyField, TextField
from .user import User

Model = db.Model

class BlogPost(Model):
    title = TextField()
    content = TextField()
    date = DateTimeField(
        default=datetime.datetime.utcnow
    )
    author = ForeignKeyField(User, backref='blogpost')  
