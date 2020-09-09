from peewee import (
    CharField,
    ForeignKeyField,
)
from base.model import (
    BaseModel
)
from apps.categories.models import (
    CategoryModel
)


class ProductModel(BaseModel):
    category = ForeignKeyField(CategoryModel, column_name='category')
    name = CharField()

    def __str__(self):
        return self.name

    class Meta:
        table_name = 'product'
