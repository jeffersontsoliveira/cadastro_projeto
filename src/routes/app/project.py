from sanic import Blueprint
from sanic.request import Request
from src.controllers.projects import ProjectController

project = Blueprint('content_project', url_prefix='/project')


@project.get('/')
async def index(request: Request):
    return await ProjectController.index(request)


@project.get('/<uid>')
async def show(request: Request, uid):
    return await ProjectController.show(request, uid)


@project.post('/')
async def store(request: Request):
    return await ProjectController.store(request)


@project.delete('/<uid>')
async def destroy(request: Request, uid):
    return await ProjectController.destroy(request, uid)


@project.put('/<uid>')
async def update(request: Request, uid):
    return await ProjectController.update(request, uid)



