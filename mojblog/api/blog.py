from freenit.api.methodviews import MethodView
from flask_smorest import Blueprint
from ..schemas.blog_post import BlogPostSchema

blueprint = Blueprint('blogs', 'blogs')

@blueprint.route('', endpoint='blog')
class BlogPostListAPI(MethodView):
    @blueprint.response(BlogPostSchema)
    @blueprint.arguments(BlogPostSchema)
    def post(self, args):
        '''Create blog post'''
        return args
