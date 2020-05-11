from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_optional
from freenit.api.methodviews import MethodView
from freenit.schemas.paging import PageInSchema, paginate
from ..schemas.blog_post import BlogPostSchema, BlogPostPageOutSchema
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
            user = User.get(id = userId)
        except User.DoesNotExist:
            abort(404, message='User not found')
        blogPost.author = user
        blogPost.save()
        return blogPost

@blueprint.route('', endpoint='list_blog_posts')
class ListBlogPostsAPI(MethodView):
#    @jwt_optional
    @blueprint.arguments(PageInSchema(), location='headers')
    @blueprint.response(BlogPostPageOutSchema)
    def get(self, pagination):
        '''List blog posts'''
#        userId = get_jwt_identity()
#        if userId is None:
#            query = BlogPost.select().where(BlogPost.published)
#        else:
        query = BlogPost.select()
        return paginate(query, pagination)

@blueprint.route('/<slug>', endpoint='get_blog_post')
class GetBlogPostAPI(MethodView):
    @blueprint.response(BlogPostSchema)
    def get(self, slug):
        '''Get blog post'''
        try:
            blogPost = BlogPost.get(slug = slug)
        except BlogPost.DoesNotExist:
            abort(404, message='Blog post not found')
        return blogPost

@blueprint.route('/<slug>', endpoint='edit_blog_post')
class EditBlogPostAPI(MethodView):
    @jwt_required
    @blueprint.arguments(BlogPostSchema(partial=True))
    @blueprint.response(BlogPostSchema)
    def patch(self, args, slug):
        '''Edit blog post'''
        try:
            blogPost = BlogPost.get(slug = slug)
        except BlogPost.DoesNotExist:
            abort(404, message='Blog post not found')
        for field in args:
            setattr(blogPost, field, args[field])
        blogPost.save()
        return blogPost

@blueprint.route('/<slug>', endpoint='delete_blog_post')
class DeleteBlogPostAPI(MethodView):
    @jwt_required
    @blueprint.response(BlogPostSchema)
    def delete(self, slug):
        '''Delete blog post'''
        try:
            blogPost = BlogPost.get(slug = slug)
        except BlogPost.DoesNotExist:
            abort(404, message='Blog post not found')
        blogPost.delete_instance()
        return blogPost
