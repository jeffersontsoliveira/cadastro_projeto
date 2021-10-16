from src.database.database import BaseModel
from src.models.user import User
from src.models.projects import Project
from datetime import datetime
import peewee

class Projectuser(BaseModel):
    name_projectuser = peewee.ForeignKeyField(Project)
    description_projectuser = peewee.ForeignKeyField(Project)
    target_projectuser = peewee.ForeignKeyField(Project)
    name_userprojectuser = peewee.ForeignKeyField(User)
    username_projectuser = peewee.ForeignKeyField(User)

