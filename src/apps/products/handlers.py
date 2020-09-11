from base.schemas import (
    BaseSchema,
    NotFoundSchema,
    BadRequestSchema,
)
from marshmallow import (
    fields,
)


class ProductSchema(BaseSchema):
    id = fields.Int(required=True)
    name = fields.Str(required=True, description='Name product')
    code = fields.Int(required=True, descriotion='Code product')
