from src.database.database import BaseModel
from datetime import datetime
from src.models.skills import Skills
from playhouse.postgres_ext import ArrayField
from datetime import date
import peewee


class User(BaseModel):
    name = peewee.CharField()
    born_date = peewee.DateField(formats=['%Y-%m-%d'])
    occupation = peewee.CharField(null=True)
    skills = peewee.ManyToManyField(Skills, backref='users')
    academic_bond = peewee.CharField()
    integration_date = peewee.DateField(null=True, formats=['%Y-%m-%d'])
    whats_app = peewee.CharField(null=True)
    remuneration = peewee.CharField(null=True)
    password = peewee.CharField()
    email = peewee.CharField(unique=True)
    admin = peewee.BooleanField(default=False)

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
            User.admin
        ]


SkillsUser = User.skills.get_through_model()






