from freenit.schemas.base import BaseSchema
from freenit.schemas.paging import PageOutSchema
from freenit.schemas.user import UserSchema
from marshmallow import fields

class BlogPostSchema(BaseSchema):
    id = fields.Integer(description='ID', dump_only=True)
    title = fields.String(description='Title', required=True)
    content = fields.String(description='Content')
    author = fields.Nested(UserSchema, dump_only=True)
    date = fields.DateTime(
        description='Time when blog post was created',
        dump_only=True,
    )
