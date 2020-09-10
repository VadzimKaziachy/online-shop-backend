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


class GistParameter(Schema):
    id = fields.Int()
