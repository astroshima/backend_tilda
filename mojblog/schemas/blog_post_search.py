from freenit.schemas.paging import PageInSchema
from marshmallow import fields

class BlogPostSearchSchema(PageInSchema):
    Search = fields.String()