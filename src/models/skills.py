from src.database.database import BaseModel
from datetime import datetime
import peewee


class Skills(BaseModel):
    skill_area = peewee.CharField()
    skill_type = peewee.CharField()
    skill_level = peewee.CharField(unique=True)

    admin = peewee.BooleanField(default=False)

    createdAt = peewee.DateTimeField(default = datetime.utcnow())