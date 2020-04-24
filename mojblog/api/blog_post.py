from freenit.api.methodviews import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..schemas.blog_post import BlogPostSchema
from ..models.blog_post import BlogPost
from ..models.user import User

blueprint = Blueprint('blogPost', 'blogPost')

@blueprint.route('', endpoint='create_blog_post')
class CreateBlogPostAPI(MethodView):
    @blueprint.response(BlogPostSchema)
    @blueprint.arguments(BlogPostSchema)
    def post(self, args):
        '''Create blog post'''
        return args
