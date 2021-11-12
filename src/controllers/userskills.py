import json

from sanic.request import Request
from sanic import response
from src.models.skills import Skills
from src.models.user import User, SkillsUser
from src.database.database import connection
from peewee_validates import ModelValidator
from playhouse.shortcuts import model_to_dict
from src.utils.serialize import Serialize
from datetime import datetime


class UserSkillsController:
    @staticmethod
    async def index_skill(uid: int):
        skill = Skills.get_or_none(id=uid)
        if skill is None:
            return response.json({'skill': 'skill not found '}, status=404)

        skills = [user.name for user in skill.users]

        if len(skills) is 0:
            return response.json({'skill': 'skill has no user associated'}, status=404)

        return response.json(skills, dumps=json.dumps, cls=Serialize)

    @staticmethod
    async def remove(id_skills: int, id_users: int):
        skill = Skills.get_or_none(id=id_skills)
        if skill is None:
            return response.json({'skill': 'skill not found '}, status=404)
        usera = User.get_or_none(id=id_users)
        print(usera)
        if usera is None:
            return response.json({'user': 'user not found '}, status=404)

        users = [user.name for user in skill.users]

        print(users)

        if usera.name not in users:
            print(usera.name)
            return response.json({'user': 'user not found '}, status=404)

        skill.users.remove(usera)

        return response.empty()

    @staticmethod
    async def remove_all(id_skills: int):
        skill = Skills.get_or_none(id=id_skills)
        if skill is None:
            return response.json({'skill': 'skill not found '}, status=404)

        user = User.select()

        skills = [model_to_dict(skill) for skill in skill.users]

        skill.users.clear()

        return response.empty()

    @staticmethod
    async def add_skill(id_skills: int, id_user: int):
        user = User.get_or_none(id=id_user)
        if user is None:
            return response.json({'user': 'user not found '}, status=404)
        skill = Skills.get_or_none(id=id_skills)
        if skill is None:
            return response.json({'skill': 'skill not found '}, status=404)

        if user in skill.users:
            return response.json({'user': 'user already has this skill'}, status=400)

        user.skills.add(skill)
        skills = [model_to_dict(user) for user in user.skills]

        return response.json(skills, dumps=json.dumps, cls=Serialize)


class SkillsUserController:
    @staticmethod
    async def index_user(uid: int):
        user = User.get_or_none(id=uid)
        if user is None:
            return response.json({'user': 'user not found'}, status=404)

        users = [[skill.skill_area, skill.skill_type, skill.skill_level] for skill in user.skills]

        if len(users) is 0:
            return response.json({'user': 'user has no skills'}, status=404)

        return response.json(users, dumps=json.dumps, cls=Serialize)

