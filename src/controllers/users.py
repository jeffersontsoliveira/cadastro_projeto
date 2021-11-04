import json

import phonenumbers
from sanic.request import Request
from sanic import response
from src.models.user import User
from src.database.database import connection
from peewee_validates import ModelValidator
from playhouse.shortcuts import model_to_dict
from src.utils.serialize import Serialize
from datetime import datetime
from phonenumbers import geocoder


class UserController:
    @staticmethod
    async def index(request: Request):
        page = 1
        size = 5
        sizes =[5, 10, 20]

        if 'page' in request.args:
            _page: str = request.args['page'][0]
            if not _page.isnumeric():
                return response.json({'pages':'arguments page must be numeric'}, status=400)

            page: int = int(_page)

        if 'size' in request.args:
            _size: str = request.args['size'][0]

            if not _size.isnumeric():
                return response.json({'size': 'argument size must be numeric'}, status=400)

            _size: int = int(_size)
            if _size in sizes:
                size = _size


        users = []
        query = User.select()

        count = query.count()
        print(f'count: {count}')
        pages = (count // size) + 1 if (count % size) > 0 else 0

        query = query.paginate(page=page, paginate_by=size)

        for user in query:
            users.append(user.json)

        data = dict()
        data['pages'] = pages
        data['users'] = users

        return response.json(data, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def show(request: Request, uid: str):

        user = User.get_or_none(id=uid)

        if user is None:
            return response.json({'user': 'user not found'}, status=404)

        return response.json(user.json, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def store(request: Request):
        with connection.atomic() as transaction:
            data = request.json

            occupations = ['backend', 'frontend', 'fullstack', 'tester', 'devops', 'ui', '']
            bonds = ['graduating', 'masters_degree', 'doctoral_student', '']
            remunerations = ['voluntary', 'paid']

            if 'occupation' not in data:
                errors = User.validate(**data)
            else:
                if data['occupation'] in occupations:
                    errors = User.validate(**data)
                else: return response.json({'user': 'occupation not found'}, status=400)

            if 'academic_bond' not in data:
                errors = User.validate(**data)
            else:
                if data['academic_bond'] in bonds:
                    errors = User.validate(**data)
                else: return response.json({'user': 'academic_bond not found'}, status=400)
            if 'whats_app' not in data:
                errors = User.validate(**data)
            else:
                if data['whats_app'].isnumeric():

                    if 8 < len(data['whats_app']) < 15:
                        whats_app_adj = phonenumbers.parse(data['whats_app'], "BR")
                        whats_app_end = phonenumbers.format_number(whats_app_adj, phonenumbers.PhoneNumberFormat.NATIONAL)
                        data['whats_app'] = whats_app_end
                    else: return response.json({'user': 'what_app must be xxxxx-xxxx'}, status=400)
                else: return response.json({'user': 'argument what_app must be numeric'}, status=400)

            if 'remuneration' not in data:
                errors = User.validate(**data)
            else:
                if data['remuneration'] in remunerations:
                    errors = User.validate(**data)
                else: return response.json({'user': 'remunerations not found'}, status=400)

            if data['born_date'] != ['%Y-%m-%d']:
                return response.json({'user': 'date must be yyyy/mm/dd'}, status=400)

            if bool(errors):
                return response.json(errors, status=400)
        user: User = User.create(**data)
        return response.json(user.json, status=201, dumps=json.dumps, cls=Serialize)


    @staticmethod
    async def update(request: Request, uid: str):
        user = User.get_or_none(id=uid)

        if user is None:
            return response.json({'user':'user not found '}, status=404)

        data = request.json.copy()
        occupations = ['backend', 'frontend', 'fullstack', 'tester', 'devops', 'ui']

        if 'occupation' not in data:
            user_dict = user.json
            user_dict.update(data)
            errors = User.validate(**data)
        else:
            if data['occupation'] in occupations:
                user_dict = user.json
                user_dict.update(data)
                errors = User.validate(**user_dict)
            else:
                return response.json({'user': 'occupation not found '}, status=400)

        if bool(errors):
            return response.json(errors, status=400)

        user_dict['updatedAt'] = datetime.utcnow()

        User.update(**user_dict).where(User.id == user.id).execute()

        return response.json(user_dict, dumps=json.dumps, cls=Serialize)





    @staticmethod
    async def destroy(request: Request, uid: str):
        user = User.get_or_none(id=uid)

        if user is None:
            return response.json({'user': 'user not found'}, status=404)

        user.delete_instance(recursive=True)

        return response.empty()