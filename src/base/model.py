import peewee
import datetime

from settings.database import DATABASE


class BaseModel(peewee.Model):
    """
     Common db model

     Fields:
        1) created - timestamp (auto on creation)
    """
    created = peewee.DateTimeField(default=datetime.datetime.now, index=True)

    class Meta:
        database = DATABASE
