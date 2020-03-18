from freenit.api import register_endpoints

def create_api(app):
    from .blog_post import blueprint as blogPost
    register_endpoints(
        app,
        '/api/v0',
        [
            blogPost,
        ]
    )
