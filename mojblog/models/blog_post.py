import datetime
from freenit.db import db
from .user import User
from peewee import DateTimeField, ForeignKeyField, TextField

Model = db.Model

class BlogPost(Model):
    title = TextField()
    content = TextField()
    date = DateTimeField(
        default=datetime.datetime.utcnow
    )
    author = ForeignKeyField(User, backref='blogpost')  
