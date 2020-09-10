from peewee import (
    CharField
)
from base.model import (
    BaseModel
)


class CategoryModel(BaseModel):
    """
    Category model.

    Fields:
        1) name - field for saving shop category;
    """

    name = CharField()

    def __str__(self):
        return self.name

    class Meta:
        table_name = 'category'
