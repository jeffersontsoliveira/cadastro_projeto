from sanic import Blueprint, response
from sanic.request import Request
from src.controllers.projects import ProjectUSer
#from src.controllers.authorization import app_authorization

projectuser = Blueprint('content_message', url_prefix='/projects')


@projectuser.get('/<uid>')
#@app_authorization()
async def index(request: Request, uid):
    return await ProjectUSer.index(request, uid)

@projectuser.delete('/<uid>')
async def destroy(request: Request, uid):
    return await ProjectUSer.destroy(request, uid)

@projectuser.patch('/<id_project:int>/user/<id_users:int>')
#@app_authorization()
async def add_user(request: Request, id_project, id_users):
    print(id_project, id_users)
    return await ProjectUSer.add_user(id_users, id_project)
