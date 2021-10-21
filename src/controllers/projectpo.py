import json

from sanic.request import Request
from sanic import response
from src.models.projects import Project, ProjectUser
from src.models.user import User
from src.database.database import connection
from peewee_validates import ModelValidator
from playhouse.shortcuts import model_to_dict
from src.utils.serialize import Serialize
from datetime import datetime


class ProjectPOController:
    # @staticmethod
    # async def index(uid: int):
    #     project = Project.get_or_none(id=uid)
    #     if project is None:
    #         return response.json({'project': 'project not found '}, status=404)
    #
    #     users = [user.username for user in project.users]
    #
    #     if len(users) is 0:
    #         return response.json({'project': 'project has no user associated'}, status=404)
    #
    #     return response.json(users, dumps=json.dumps, cls=Serialize)
    #
    # @staticmethod
    # async def show(uid: int):
    #     user = User.get_or_none(id=uid)
    #     if user is None:
    #         return response.json({'user': 'user not found in a project'}, status=404)
    #
    #     projects = [project.name_project for project in user.projects]
    #
    #     if len(projects) is 0:
    #         return response.json({'user': 'user is not in a project'}, status=404)
    #
    #     return response.json(projects, dumps=json.dumps, cls=Serialize)
    #
    # @staticmethod
    # async def destroy(id_project: int, id_users: int):
    #     project = Project.get_or_none(id=id_project)
    #     if project is None:
    #         return response.json({'project': 'project not found '}, status=404)
    #     usera = User.get_or_none(id=id_users)
    #     print(usera)
    #     if usera is None:
    #         return response.json({'user': 'user not found '}, status=404)
    #
    #     users = [user.name for user in project.users]
    #
    #     print(users)
    #
    #     if usera.name not in users:
    #         print(usera.username)
    #         return response.json({'user': 'user not found '}, status=404)
    #
    #     project.users.remove(usera)
    #
    #     return response.empty()
    #
    # @staticmethod
    # async def destroy_all(id_project: int):
    #     project = Project.get_or_none(id=id_project)
    #     if project is None:
    #         return response.json({'project': 'project not found '}, status=404)
    #
    #     user = User.select()
    #
    #     users = [model_to_dict(user) for user in project.users]
    #
    #     project.users.clear()
    #
    #     return response.empty()

    @staticmethod
    async def add_po(id_project: int, id_users: int):
        user = User.get(id=id_users)
        project = Project.get(id=id_project)

        project.users.add(user)

        return response.json(project.json, status=201, dumps=json.dumps, cls=Serialize)



