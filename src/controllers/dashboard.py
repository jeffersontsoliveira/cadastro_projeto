import json

from sanic.request import Request
from sanic import response
from src.models.projects import Project
from src.models.user import User
from src.database.database import connection
from src.models.dashboard import Lists, Notes
from peewee_validates import ModelValidator
from playhouse.shortcuts import model_to_dict
from src.utils.serialize import Serialize
from datetime import datetime


class ListsController:
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

        lists = []
        query = Lists.select()

        count = query.count()
        pages = (count // size) + 1 if (count % size) > 0 else 0

        query = query.paginate(page=page, paginate_by=size)

        for listo in query:
            lists.append(listo.json)

        data = dict()
        data['pages'] = pages
        data['projects'] = lists

        return response.json(data, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def show(request: Request, uid: str):
        list_con = Lists.get_or_none(id=uid)

        if list_con is None:
            return response.json({'list': 'list not found'}, status=404)

        return response.json(list_con.json, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def store(request: Request):
        with connection.atomic() as transaction:
            data = request.json

            errors = Lists.validate(**data)

            if bool(errors):
                return response.json(errors, status=400)

            lists: Lists = Lists.create(**data)

        return response.json(lists.json, status=201, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def update(request: Request, uid: str):
        list = Lists.get_or_none(id=uid)

        if list is None:
            return response.json({'project': 'project not found '}, status=404)

        data = request.json.copy()

        list_dict = list.json
        list_dict.update(data)

        errors = Lists.validate(**list_dict)

        if bool(errors):
            return response.json(errors, status=400)

        list_dict['updatedAt'] = datetime.utcnow()

        Lists.update(**list_dict).where(Lists.id == list.id).execute()

        return response.json(list_dict, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def destroy(request: Request, uid: str):
        list = Lists.get_or_none(id=uid)

        if list is None:
            return response.json({'project': 'project not found'}, status=404)

        list.delete_instance(recursive=True)

        return response.empty()

