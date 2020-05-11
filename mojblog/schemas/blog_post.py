import sys
from marshmallow import fields
from freenit.schemas.base import BaseSchema
from freenit.schemas.paging import PageOutSchema
from freenit.schemas.user import UserSchema

class BlogPostSchema(BaseSchema):
    id = fields.Integer(description='ID', dump_only=True)
    slug = fields.String(description='Slug', dump_only=True)
    title = fields.String(description='Title', required=True)
    content = fields.String(description='Content')
    date = fields.DateTime(
        description='Time when blog post was created',
        dump_only=True,
    )
    author = fields.Nested(UserSchema, dump_only=True)
    published = fields.Boolean(description='Published', default=False)

PageOutSchema(BlogPostSchema, sys.modules[__name__])
