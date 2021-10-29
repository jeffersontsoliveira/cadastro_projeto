from src.database.database import BaseModel
from datetime import datetime
from datetime import date
import peewee


class User(BaseModel):
    name = peewee.CharField()
    born_date = peewee.DateField(null=True)
    occupation = peewee.CharField(null=True)
    skills = peewee.TextField(null=True)
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






