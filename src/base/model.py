import peewee

from settings.database import DATABASE


class BaseModel(peewee.Model):
    class Meta:
        database = DATABASE
