from src.database.database import BaseModel
from datetime import datetime
import peewee


class User(BaseModel):
    name = peewee.CharField()
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    email = peewee.CharField(unique=True)
    admim = peewee.BooleanField(default=False)

    createdAt = peewee.DateTimeField(default = datetime.utcnow())
    updatedAt = peewee.DateTimeField(default = datetime.utcnow())

    class Meta:
        table_name = '_user'

    @property
    def exclude(self):
        return None

    @exclude.getter
    def exclude(self):
        return [
            User.password,
            User.admim
        ]






