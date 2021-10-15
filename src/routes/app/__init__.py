from sanic import Blueprint
from .user import user
from .project import project

app = Blueprint.group([user, project], url_prefix='/app')


