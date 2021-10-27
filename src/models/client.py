from src.database.database import BaseModel
from datetime import datetime
import peewee


class Client(BaseModel):
    company = peewee.CharField()
    fictitious_name = peewee.CharField(unique=True)
    admim = peewee.BooleanField(default=False)

    createdAt = peewee.DateTimeField(default = datetime.utcnow())
    updatedAt = peewee.DateTimeField(default = datetime.utcnow())
