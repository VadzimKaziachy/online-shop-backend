from peewee import (
    CharField
)
from base.model import (
    BaseModel
)


class CategoryModel(BaseModel):
    name = CharField()

    def __str__(self):
        return self.name

    class Meta:
        table_name = 'category'
