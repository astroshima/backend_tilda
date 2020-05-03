from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_optional
from freenit.api.methodviews import MethodView
from freenit.schemas.paging import PageInSchema, paginate
from ..schemas.blog_post import BlogPostSchema, PageOutSchema
from ..models.blog_post import BlogPost
from ..models.user import User

blueprint = Blueprint('blogpost', 'blogpost')

@blueprint.route('', endpoint='create_blog_post')
class CreateBlogPostAPI(MethodView):
    @jwt_required
    @blueprint.response(BlogPostSchema)
    @blueprint.arguments(BlogPostSchema)
    def post(self, args):
        '''Create blog post'''
        blogPost = BlogPost(**args)
        userId = get_jwt_identity()
        try:
            user = User.get(id=userId)
        except User.DoesNotExist:
            abort(404, message='User not found')
        blogPost.author = user
        blogPost.save()
        return blogPost


