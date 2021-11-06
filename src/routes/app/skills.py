from sanic import Blueprint, response
from sanic.request import Request
from src.controllers.skills import SkillController
#from src.controllers.authorization import app_authorization

skills = Blueprint('content_skills', url_prefix='/skills')


@skills.get('/')
async def index(request: Request):
    return await SkillController.index(request)


@skills.get('/<uid:int>')
async def show(request: Request, uid):
    return await SkillController.show(request, uid)


@skills.post('/')
async def store(request: Request):
    return await SkillController.store(request)


@skills.put('/<uid:int>')
async def update(request: Request, uid):
    return await SkillController.update(request, uid)


@skills.delete('/<uid:int>')
async def destroy(request: Request, uid):
    return await SkillController.destroy(request, uid)





