from sanic import Blueprint, response
from sanic.request import Request
from src.controllers.projectuser import ProjectUSerController
#from src.controllers.authorization import app_authorization

projectuser = Blueprint('content_projectuser', url_prefix='/projects')


@projectuser.get('/<uid:int>/users')
#@app_authorization()
async def index(request: Request, uid):
    return await ProjectUSerController.index(uid)


@projectuser.get('/users/<uid:int>')
#@app_authorization()
async def show(request: Request, uid):
    return await ProjectUSerController.show(uid)


@projectuser.delete('/<id_project:int>/users/<id_users:int>')
async def destroy(request: Request, id_project, id_users):
    return await ProjectUSerController.destroy(id_project, id_users)


@projectuser.delete('/users/delete/<id_project:int>')
async def destroy_all(request: Request, id_project):
    return await ProjectUSerController.destroy_all(id_project)


@projectuser.patch('/<id_project:int>/user/<id_users:int>')
#@app_authorization()
async def add_user(request: Request, id_project, id_users):
    return await ProjectUSerController.add_user(id_project, id_users)
