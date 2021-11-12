from sanic import Blueprint
from .user import user
from .project import project
from .projectuser import projectuser, userproject
from .client import client
from .skills import skills
from .userskills import userskills, skillsusers

app = Blueprint.group([user, project, projectuser, userproject, client, skills, userskills, skillsusers], url_prefix='/app')


