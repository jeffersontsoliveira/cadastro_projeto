from sanic import Blueprint
from .user import user
from .project import project
from .projectuser import projectuser
from .po import projectpo

app = Blueprint.group([user, project, projectuser, projectpo], url_prefix='/app')


