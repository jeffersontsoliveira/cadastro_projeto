from sanic import Blueprint
from .user import user
from .project import project
from .projectuser import projectuser

app = Blueprint.group([user, project, projectuser], url_prefix='/app')


