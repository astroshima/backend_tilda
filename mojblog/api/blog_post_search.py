from flask_smorest import Blueprint
from freenit.api.methodviews import MethodView
from freenit.schemas.paging import PageInSchema, paginate
from ..schemas.blog_post import BlogPostPageOutSchema
from ..schemas.blog_post_search import BlogPostSearchSchema
from ..models.blog_post import BlogPost
from ..models.user import User

blueprint = Blueprint('blogpostsearch', 'blogpostsearch')

@blueprint.route('', endpoint='search_blog_posts_by_title')
class SearchBlogPostsByTitleApi(MethodView):
    @blueprint.arguments(BlogPostSearchSchema(), location='headers')
    @blueprint.response(BlogPostPageOutSchema)
    def get(self, headersArgs):
        """Search blog posts by title"""
        print(headersArgs)
        titleParam = headersArgs.get('Search','')
        sameTitlePartBlogPosts = BlogPost.select().where(BlogPost.published,
                                                        BlogPost.title.contains(titleParam)).order_by(BlogPost.author)
        return paginate(sameTitlePartBlogPosts, headersArgs)