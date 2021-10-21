from sanic import Blueprint, response
from sanic.request import Request
from src.controllers.projectpo import ProjectPOController
#from src.controllers.authorization import app_authorization

projectpo = Blueprint('content_po', url_prefix='/po')


# @projectuser.get('/<uid>')
# #@app_authorization()
# async def index(request: Request, uid):
#     return await ProjectUSerController.index(uid)
#
#
# @projectuser.get('/user/<uid>')
# #@app_authorization()
# async def show(request: Request, uid):
#     return await ProjectUSerController.show(uid)
#
#
# @projectuser.delete('/<id_project:int>/user/<id_users:int>')
# async def destroy(request: Request, id_project, id_users):
#     return await ProjectUSerController.destroy(id_project, id_users)
#
#
# @projectuser.delete('/alluser/<id_project:int>')
# async def destroy_all(request: Request, id_project):
#     return await ProjectUSerController.destroy_all(id_project)


@projectpo.patch('/<id_project:int>/user/<id_users:int>')
#@app_authorization()
async def add_po(request: Request, id_project, id_users):
    return await ProjectPOController.add_po(id_project, id_users)
