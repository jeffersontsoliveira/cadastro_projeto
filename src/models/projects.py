from src.database.database import BaseModel
from src.models.user import User
from src.models.client import Client
from datetime import datetime
import peewee


class Project(BaseModel):
    name_project = peewee.CharField(unique=True)
    description = peewee.CharField()
    clients = peewee.ManyToManyField(Client, backref='projects')
    po = peewee.ForeignKeyField(User,null=True, backref='po')
    scrum_master = peewee.ForeignKeyField(User, null=True, backref='scrum')
    target = peewee.CharField()
    users = peewee.ManyToManyField(User, backref='projects')
    createdAt = peewee.DateTimeField(default=datetime.utcnow())
    updatedAt = peewee.DateTimeField(default=datetime.utcnow())


ProjectUser = Project.users.get_through_model()
ProjectClient = Project.clients.get_through_model()


