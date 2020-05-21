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

@blueprint.route('', endpoint='list_published_blog_posts')
class ListPublishedBlogPostsAPI(MethodView):
    @blueprint.arguments(PageInSchema(), location='headers')
    @blueprint.response(BlogPostPageOutSchema)
    def get(self, pagination):
        '''List published blog posts sorted by user_id'''
        sortedPublishedBlogPosts = BlogPost.select().where(BlogPost.published).order_by(BlogPost.author)
        return paginate(sortedPublishedBlogPosts, pagination)

@blueprint.route('/<blog_post_id>', endpoint='get_blog_post_by_blog_post_id')
class GetBlogPostByBlogPostIdAPI(MethodView):
    @blueprint.response(BlogPostSchema)
    def get(self, blog_post_id):
        '''Get blog post by blog_post_id'''
        try:
            blogPost = BlogPost.get(id = blog_post_id)
        except BlogPost.DoesNotExist:
            abort(404, message='Blog post not found')
        try:
            blogPost2 = BlogPost.get( id = int(blog_post_id) + 1 )
        except BlogPost.DoesNotExist:
            abort(404, message='Blog post not found')
        print(blogPost.slug)    #: prvi-naslov
        print(blogPost2.slug)    #: drugi-blog-post
        print(BlogPost.slug)    #: <TextField: BlogPost.slug>
        return blogPost

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

@blueprint.route('/user/<userId>', endpoint='list_blog_posts_by_user')
class ListBlogPostsByUserAPI(MethodView):
    @blueprint.arguments(PageInSchema(), location='headers')
    @blueprint.response(BlogPostPageOutSchema)
    def get(self, pagination, userId):
        '''List blog posts by user'''
        try:
            user = User.get(id=userId)
        except User.DoesNotExist:
            abort(404, message='User not found')
        blogPostsByUser = BlogPost.select().where(BlogPost.author == user)
        return paginate(blogPostsByUser, pagination)

