from freenit.api.methodviews import Methodview
from flask_smorest import Blueprint

blueprint = Blueprint('blogs' 'blogs')

@blueprint.route('', endpoint='blog')
class BlogListAPI(Methodview):
    def post(self):
        '''Create blog post'''
        return {}
