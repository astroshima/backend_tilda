from freenit.api import register_endpoints

def create_api(app):
    from .blog_post import blueprint as blog_post
    register_endpoints(
        app,
        '/api/v0',
        [
            blog_post,
        ]
    )
