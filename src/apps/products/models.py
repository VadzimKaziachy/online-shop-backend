from peewee import (
    CharField,
    IntegerField,
    ForeignKeyField,
)
from base.model import (
    BaseModel
)
from apps.categories.models import (
    CategoryModel
)


class ProductModel(BaseModel):
    """
    Product model, which has category.

    Fields:
        1) name - field for saving product name;
        2) code - field for saving unique product code;
        3) category - field for saving link to CategoryModel.
    """

    name = CharField(verbose_name='Name')
    code = IntegerField(verbose_name='Code')
    category = ForeignKeyField(CategoryModel, column_name='category')

    def __str__(self):
        return self.name

    class Meta:
        table_name = 'product'
