from sanic import Blueprint
from .user import user
from .project import project
from .projectuser import projectuser
from .client import client
from .skills import skills
from .userskills import userskills

app = Blueprint.group([user, project, projectuser, client, skills, userskills], url_prefix='/app')


