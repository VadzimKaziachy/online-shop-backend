from base.schema import (
    BaseSchema,
    NotFoundSchema,
)
from marshmallow import (
    fields,
    Schema,
)


class CategorySchema(BaseSchema):
    """Complete category schema"""

    id = fields.Int(
        required=True,
    )
    created = fields.DateTime(
        required=False,
        description='The time at which the category was created in the database',
    )
    name = fields.Str(
        required=True,
        description='Name of the category',
    )


class CategoryCreateSchema(CategorySchema):
    class Meta:
        ordered = True
        exclude = ('created', 'id')


class IdParameter(Schema):
    id = fields.Int()
