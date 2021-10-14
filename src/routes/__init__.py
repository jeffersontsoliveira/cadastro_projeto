from sanic import Blueprint
from scr.routes.user import user


routes = Blueprint.group([user], url_prefix='/app')



