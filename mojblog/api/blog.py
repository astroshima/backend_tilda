from freenit.api.methodviews import MethodView
from flask_smorest import Blueprint

blueprint = Blueprint('blogs', 'blogs')

@blueprint.route('', endpoint='blog')
class BlogListAPI(MethodView):
    def post(self):
        '''Create blog post'''
        return {}
