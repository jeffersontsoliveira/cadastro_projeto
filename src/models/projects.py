from src.database.database import BaseModel
from src.models.user import User
from datetime import datetime
import peewee


class Project(BaseModel):
    name_project = peewee.CharField()
    description = peewee.CharField()
    target = peewee.CharField()

    createdAt = peewee.DateTimeField(default=datetime.utcnow())
    updatedAt = peewee.DateTimeField(default=datetime.utcnow())
