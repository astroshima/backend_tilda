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

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = self.title.lower().replace(" ", "-")
        super(BlogPost, self).save(*args, **kwargs)
