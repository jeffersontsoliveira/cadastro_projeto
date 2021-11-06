import json

from sanic.request import Request
from sanic import response
from src.models.skills import Skills
from src.database.database import connection
from src.utils.serialize import Serialize
from datetime import datetime


class SkillController:
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

        skills = []
        query = Skills.select()

        count = query.count()
        print(f'count: {count}')
        pages = (count // size) + 1 if (count % size) > 0 else 0

        query = query.paginate(page=page, paginate_by=size)

        for skill in query:
            skills.append(skill.json)

        data = dict()
        data['pages'] = pages
        data['skills'] = skills

        return response.json(data, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def show(request: Request, uid: str):
        skill = Skills.get_or_none(uid)

        if skill is None:
            return response.json({'skill': 'skill not found'}, status=404)

        return response.json(skill.json, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def store(request: Request):
        with connection.atomic() as transaction:
            data = request.json

            errors = Skills.validate(**data)

            if bool(errors):
                return response.json(errors, status=400)

            skill: Skills = Skills.create(**data)

        return response.json(skill.json, status=201, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def update(request: Request, uid):
        skill = Skills.get_or_none(uid)

        if skill is None:
            return response.json({'skill': 'skill not found'}, status=404)

        data = request.json.copy()

        skill_dict = skill.json
        skill_dict.update(data)

        errors = Skills.validate(**skill_dict)

        if bool(errors):
            return response.json(errors, status=400)

        skill_dict['updatedAt'] = datetime.utcnow()

        Skills.update(**skill_dict).where(Skills.id == skill.id).execute()

        return response.json(skill_dict, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def destroy(request: Request, uid: int):
        skill = Skills.get_or_none(id=uid)

        if skill is None:
            return response.json({'skill': 'skill not found'}, status=404)

        skill.delete_instance(recursive=True)

        return response.json({'skill': 'skill deleted'}, status=201)


