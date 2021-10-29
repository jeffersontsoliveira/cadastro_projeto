from src.database.database import BaseModel
from src.models.user import User
from datetime import datetime
import peewee


class Lists(BaseModel):
    name_list = peewee.CharField()
    description = peewee.CharField()
    current_user = peewee.ForeignKeyField(User, null=True, backref='lists')
    target = peewee.CharField(null=True)
    createdAt = peewee.DateTimeField(default=datetime.utcnow())
    updatedAt = peewee.DateTimeField(default=datetime.utcnow())


class Notes(BaseModel):
    new_note = peewee.CharField()
    description = peewee.CharField()
    current_user = peewee.ForeignKeyField(User, null=True, backref='lists')
    target = peewee.CharField()
    createdAt = peewee.DateTimeField(default=datetime.utcnow())
    updatedAt = peewee.DateTimeField(default=datetime.utcnow())

