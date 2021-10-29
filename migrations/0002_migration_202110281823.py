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
    createdAt = DateTimeField(default=datetime.datetime(2021, 10, 28, 22, 23, 6, 659083))
    updatedAt = DateTimeField(default=datetime.datetime(2021, 10, 28, 22, 23, 6, 659104))
    class Meta:
        table_name = "client"


@snapshot.append
class User(peewee.Model):
    name = CharField(max_length=255)
    born_date = DateField(null=True)
    skills = TextField(null=True)
    password = CharField(max_length=255)
    email = CharField(max_length=255, unique=True)
    admim = BooleanField(default=False)
    createdAt = DateTimeField(default=datetime.datetime(2021, 10, 28, 22, 23, 6, 658221))
    updatedAt = DateTimeField(default=datetime.datetime(2021, 10, 28, 22, 23, 6, 658243))
    occupation = CharField(max_length=['Frontend', 'Backend', 'Test', 'UI/UX'])
    class Meta:
        table_name = "_user"


@snapshot.append
class Lists(peewee.Model):
    name_list = CharField(max_length=255)
    description = CharField(max_length=255)
    current_user = snapshot.ForeignKeyField(backref='lists', index=True, model='user', null=True)
    target = CharField(max_length=255)
    createdAt = DateTimeField(default=datetime.datetime(2021, 10, 28, 22, 23, 6, 660390))
    updatedAt = DateTimeField(default=datetime.datetime(2021, 10, 28, 22, 23, 6, 660411))
    class Meta:
        table_name = "lists"


@snapshot.append
class Notes(peewee.Model):
    new_note = CharField(max_length=255)
    description = CharField(max_length=255)
    current_user = snapshot.ForeignKeyField(backref='lists', index=True, model='user', null=True)
    target = CharField(max_length=255)
    createdAt = DateTimeField(default=datetime.datetime(2021, 10, 28, 22, 23, 6, 660735))
    updatedAt = DateTimeField(default=datetime.datetime(2021, 10, 28, 22, 23, 6, 660755))
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
    createdAt = DateTimeField(default=datetime.datetime(2021, 10, 28, 22, 23, 6, 659460))
    updatedAt = DateTimeField(default=datetime.datetime(2021, 10, 28, 22, 23, 6, 659481))
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


def forward(old_orm, new_orm):
    user = new_orm['user']
    return [
        # Apply default value '' to the field user.occupation
        user.update({user.occupation: ''}).where(user.occupation.is_null(True)),
    ]


def backward(old_orm, new_orm):
    user = new_orm['user']
    return [
        # Apply default value '' to the field user.username
        user.update({user.username: ''}).where(user.username.is_null(True)),
    ]
