from base.schema import BaseSchema
from marshmallow import (
    fields,
)


class CategorySchema(BaseSchema):
    """Complete category schema"""

    id = fields.Int(
        required=True,
    )
    name = fields.Str(
        required=True,
        description='Name of the category',
    )
    created = fields.DateTime(
        required=False,
        description='The time at which the category was created in the database',
    )


class CategoryCreateSchema(CategorySchema):
    class Meta:
        ordered = True
        exclude = ('created', 'id')

