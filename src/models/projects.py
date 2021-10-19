from src.database.database import BaseModel
from src.models.user import User
from datetime import datetime
import peewee


class Project(BaseModel):
    name_project = peewee.CharField(unique=True)
    description = peewee.CharField()
    target = peewee.CharField()
    users = peewee.ManyToManyField(User, backref='projects')

    createdAt = peewee.DateTimeField(default=datetime.utcnow())
    updatedAt = peewee.DateTimeField(default=datetime.utcnow())


ProjectUser = Project.users.get_through_model()
