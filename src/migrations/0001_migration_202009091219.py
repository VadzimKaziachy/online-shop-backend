# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class CategoryModel(peewee.Model):
    name = CharField(max_length=255)
    class Meta:
        table_name = "category"


@snapshot.append
class ProductModel(peewee.Model):
    category = snapshot.ForeignKeyField(column_name='category', index=True, model='categorymodel')
    name = CharField(max_length=255)
    class Meta:
        table_name = "product"


