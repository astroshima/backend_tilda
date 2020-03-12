from freenit.api.methodviews import MethodView
from flask_smorest import Blueprint
from ..schemas.blog_post import BlogPostSchema

blueprint = Blueprint('blog', 'blog')

@blueprint.route('/post', endpoint='create_blog_post')
class CreateBlogPostAPI(MethodView):
    @blueprint.response(BlogPostSchema)
    @blueprint.arguments(BlogPostSchema)
    def post(self, args):
        '''Create blog post'''
        return args
