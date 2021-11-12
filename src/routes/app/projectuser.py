from sanic import Blueprint, response
from sanic.request import Request
from src.controllers.projectuser import ProjectUSerController
from src.controllers.projectuser import UserProjectController
#from src.controllers.authorization import app_authorization

projectuser = Blueprint('content_projectuser', url_prefix='C/<pid:int>/users')
userproject = Blueprint('content_userproject', url_prefix='/user/<uid:int>/projects')


@projectuser.get('/')
#@app_authorization()
async def list_users(request: Request, pid):
    return await ProjectUSerController.index(pid)


@projectuser.delete('/')
async def remove_all_users(request: Request, pid):
    return await ProjectUSerController.destroy_all(pid)


@projectuser.post('/<uid:int>')
#@app_authorization()
async def add_user(request: Request, pid, uid):
    return await ProjectUSerController.add_user(pid, uid)


@projectuser.delete('/<uid:int>')
async def remove_user(request: Request, pid, uid):
    return await ProjectUSerController.destroy(pid, uid)


@userproject.get('/')
#@app_authorization()
async def list_all_project(request: Request, uid):
    return await UserProjectController.index(uid)
