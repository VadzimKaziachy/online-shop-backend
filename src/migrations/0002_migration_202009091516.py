# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class CategoryModel(peewee.Model):
    created = DateTimeField(default=datetime.datetime.now, index=True)
    name = CharField(max_length=255)
    class Meta:
        table_name = "category"


@snapshot.append
class ProductModel(peewee.Model):
    created = DateTimeField(default=datetime.datetime.now, index=True)
    name = CharField(max_length=255)
    code = IntegerField()
    category = snapshot.ForeignKeyField(column_name='category', index=True, model='categorymodel')
    class Meta:
        table_name = "product"


def forward(old_orm, new_orm):
    categorymodel = new_orm['categorymodel']
    productmodel = new_orm['productmodel']
    return [
        # Apply default value datetime.datetime(2020, 9, 9, 15, 16, 52, 257934) to the field categorymodel.created
        categorymodel.update({categorymodel.created: datetime.datetime(2020, 9, 9, 15, 16, 52, 257934)}).where(categorymodel.created.is_null(True)),
        # Apply default value datetime.datetime(2020, 9, 9, 15, 16, 52, 258041) to the field productmodel.created
        productmodel.update({productmodel.created: datetime.datetime(2020, 9, 9, 15, 16, 52, 258041)}).where(productmodel.created.is_null(True)),
        # Apply default value 0 to the field productmodel.code
        productmodel.update({productmodel.code: 0}).where(productmodel.code.is_null(True)),
    ]
