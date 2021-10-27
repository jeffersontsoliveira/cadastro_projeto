from sanic import Blueprint, response
from sanic.request import Request
from src.controllers.client import ClientController
#from src.controllers.authorization import app_authorization

client = Blueprint('content_client', url_prefix='/clients')


@client.get('/')
async def index(request: Request):
    return await ClientController.index(request)


@client.get('/<uid:int>')
async def show(request: Request, uid):
    return await ClientController.show(request, uid)


@client.post('/')
async def store(request: Request):
    return await ClientController.store(request)


@client.put('/<uid:int>')
async def update(request: Request, uid):
    return await ClientController.update(request, uid)


@client.delete('/<uid:int>')
async def destroy(request: Request, uid):
    return await ClientController.destroy(request, uid)





