from sanic import Blueprint, response
from sanic.request import Request
from src.controllers.userskills import UserSkillsController
from src.controllers.userskills import SkillsUserController
#from src.controllers.authorization import app_authorization

userskills = Blueprint('content_userskills', url_prefix='/userskills/<id_skills:int>/users')

skillsusers = Blueprint('content_skillusers', url_prefix='/skillsusers/<id_users:int>/skills')


@userskills.get('/')
#@app_authorization()
async def index_skill(request: Request, id_skills):
    return await UserSkillsController.index_skill(id_skills)


@userskills.delete('/<id_users:int>')
async def remove(request: Request, id_skills, id_users):
    return await UserSkillsController.remove(id_skills, id_users)


@userskills.delete('/delete')
async def remove_all(request: Request, id_skills):
    return await UserSkillsController.remove_all(id_skills)


@userskills.post('/<id_users:int>')
#@app_authorization()
async def add_user(request: Request, id_skills, id_users):
    return await UserSkillsController.add_skill(id_skills, id_users)


@skillsusers.get('/')
#@app_authorization()
async def index_user(request: Request, id_users):
    return await SkillsUserController.index_user(id_users)
