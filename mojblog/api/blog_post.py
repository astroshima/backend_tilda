from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..schemas.blog_post import BlogPostSchema
from ..models.blog_post import BlogPost
from ..models.user import User

blueprint = Blueprint('blogpost', 'blogpost')

@blueprint.route('', methods=['POST'], endpoint='create_blog_post')
@jwt_required
@blueprint.response(BlogPostSchema)
@blueprint.arguments(BlogPostSchema)
def createBlogPost(args):
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
