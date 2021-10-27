from sanic import Blueprint
from sanic.request import Request
from src.controllers.dashboard import ListsController

dashb = Blueprint('content_lists', url_prefix='/dashboard')


@dashb.get('/')
async def index(request: Request):
    return await ListsController.index(request)


@dashb.get('/<uid:int>')
async def show(request: Request, uid):
    return await ListsController.show(request, uid)


@dashb.post('/')
async def store(request: Request):
    return await ListsController.store(request)


@dashb.delete('/<uid:int>')
async def destroy(request: Request, uid):
    return await ListsController.destroy(request, uid)


@dashb.put('/<uid:int>')
async def update(request: Request, uid):
    return await ListsController.update(request, uid)



