from sanic import Blueprint, response
from sanic.request import Request
from scr.controllers.message import MessageController

message = Blueprint('content_messege', url_prefix='/message')


@message.middlewares('request')
async def middleware(request: Request):
    pass


@message.get('/')
async def index(request: Request):
    return await MessageController.index(request)

@message.post('/')
async def store(request: Request):
    return await MessageController.store(request)



