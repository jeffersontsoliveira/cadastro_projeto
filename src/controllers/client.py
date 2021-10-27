import json

from sanic.request import Request
from sanic import response
from src.models.client import Client
from src.database.database import connection
from src.utils.serialize import Serialize
from datetime import datetime


class ClientController:
    @staticmethod
    async def index(request: Request):
        page = 1
        size = 5
        sizes = [5, 10, 20]

        if 'page' in request.args:
            _page: str = request.args['page'][0]
            if not _page.isnumeric():
                return response.json({'pages': 'arguments page must be numeric'}, status=400)

            page: int = int(_page)

        if 'size' in request.args:
            _size: str = request.args['size'][0]

            if not _size.isnumeric():
                return response.json({'size': 'argument size must be numeric'}, status=400)

            _size: int = int(_size)
            if _size in sizes:
                size = _size

        clients = []
        query = Client.select()

        count = query.count()
        print(f'count: {count}')
        pages = (count // size) + 1 if (count % size) > 0 else 0

        query = query.paginate(page=page, paginate_by=size)

        for client in query:
            clients.append(client.json)

        data = dict()
        data['pages'] = pages
        data['clients'] = clients

        return response.json(data, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def show(request: Request, uid: str):
        client = Client.get_or_none(uid)

        if client is None:
            return response.json({'client': 'client not found'}, status=404)

        return response.json(client.json, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def store(request: Request):
        with connection.atomic() as transaction:
            data = request.json

            errors = Client.validate(**data)

            if bool(errors):
                return response.json(errors, status=400)

            client: Client = Client.create(**data)

        return response.json(client.json, status=201, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def update(request: Request, uid):
        client = Client.get_or_none(uid)

        if client is None:
            return response.json({'client': 'client not found'}, status=404)

        data = request.json.copy()

        client_dict = client.json
        client_dict.update(data)

        errors = Client.validate(**client_dict)

        if bool(errors):
            return response.json(errors, status=400)

        client_dict['updatedAt'] = datetime.utcnow()

        Client.update(**client_dict).where(Client.id == client.id).execute()

        return response.json(client_dict, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def destroy(request: Request, uid: int):
        client = Client.get_or_none(id=uid)

        if client is None:
            return response.json({'client': 'client not found'}, status=404)

        client.delete_instance(recursive=True)

        return response.json({'client': 'client deleted'}, status=201)


