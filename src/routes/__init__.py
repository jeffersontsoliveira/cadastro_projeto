from sanic import Blueprint
from .app import app
#from .session import session


routes = Blueprint.group(app)