# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Client(peewee.Model):
    company = CharField(max_length=255)
    fictitious_name = CharField(max_length=255, unique=True)
    admim = BooleanField(default=False)
    createdAt = DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 50, 33, 234006))
    updatedAt = DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 50, 33, 234026))
    class Meta:
        table_name = "client"


@snapshot.append
class User(peewee.Model):
    name = CharField(max_length=255)
    username = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)
    email = CharField(max_length=255, unique=True)
    admim = BooleanField(default=False)
    createdAt = DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 50, 33, 233336))
    updatedAt = DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 50, 33, 233358))
    class Meta:
        table_name = "_user"


@snapshot.append
class Lists(peewee.Model):
    name_list = CharField(max_length=255)
    description = CharField(max_length=255)
    current_user = snapshot.ForeignKeyField(backref='lists', index=True, model='user', null=True)
    target = CharField(max_length=255)
    createdAt = DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 50, 33, 236104))
    updatedAt = DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 50, 33, 236116))
    class Meta:
        table_name = "lists"


@snapshot.append
class Notes(peewee.Model):
    new_note = CharField(max_length=255)
    description = CharField(max_length=255)
    current_user = snapshot.ForeignKeyField(backref='lists', index=True, model='user', null=True)
    target = CharField(max_length=255)
    createdAt = DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 50, 33, 236418))
    updatedAt = DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 50, 33, 236431))
    class Meta:
        table_name = "notes"


@snapshot.append
class Project(peewee.Model):
    name_project = CharField(max_length=255, unique=True)
    description = CharField(max_length=255)
    clients = snapshot.ForeignKeyField(backref='projects', index=True, model='client', null=True)
    po = snapshot.ForeignKeyField(backref='po', index=True, model='user', null=True)
    scrum_master = snapshot.ForeignKeyField(backref='scrum', index=True, model='user', null=True)
    target = CharField(max_length=255)
    createdAt = DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 50, 33, 234543))
    updatedAt = DateTimeField(default=datetime.datetime(2021, 10, 27, 0, 50, 33, 234563))
    class Meta:
        table_name = "project"


@snapshot.append
class ProjectUserThrough(peewee.Model):
    project = snapshot.ForeignKeyField(index=True, model='project')
    user = snapshot.ForeignKeyField(index=True, model='user')
    class Meta:
        table_name = "project__user_through"
        indexes = (
            (('project', 'user'), True),
            )


