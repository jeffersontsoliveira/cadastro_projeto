from sanic import Blueprint, response
from sanic.request import Request
from src.controllers.userskills import UserSkillsController
#from src.controllers.authorization import app_authorization

userskills = Blueprint('content_userskills', url_prefix='/userskills')


@userskills.get('/<uid:int>/users')
#@app_authorization()
async def index_skill(request: Request, uid):
    return await UserSkillsController.index_skill(uid)


@userskills.get('/users/<uid:int>')
#@app_authorization()
async def index_user(request: Request, uid):
    return await UserSkillsController.index_user(uid)


@userskills.delete('/<id_skills:int>/users/<id_users:int>')
async def destroy(request: Request, id_project, id_users):
    return await UserSkillsController.destroy(id_project, id_users)


@userskills.delete('/users/delete/<id_skills:int>')
async def destroy_all(request: Request, id_project):
    return await UserSkillsController.destroy_all(id_project)


@userskills.patch('/<id_skills:int>/user/<id_users:int>')
#@app_authorization()
async def add_user(request: Request, id_skills, id_users):
    return await UserSkillsController.add_skill(id_skills, id_users)
