from sanic import Blueprint, response
from sanic.request import Request
from src.controllers.projectusers import ProjectuserController
#from src.controllers.authorization import app_authorization


projectuser = Blueprint('content_message', url_prefix='/projectuser')


@projectuser.get('/<uid>')
#@app_authorization()
async def index(request: Request, uid):
    return await ProjectuserController.index(request, uid)

@projectuser.delete('/<uid>')
async def destroy(request: Request, uid):
    return await ProjectController.destroy(request, uid)

@projectuser.post('/')
#@app_authorization()
async def store(request: Request):
    return await ProjectuserController.store(request)
