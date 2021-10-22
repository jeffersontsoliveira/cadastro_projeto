from sanic import Blueprint
from .user import user
from .project import project
from .projectuser import projectuser
from .client import client

app = Blueprint.group([user, project, projectuser, client], url_prefix='/app')


