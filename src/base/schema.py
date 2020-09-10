from marshmallow import (
    fields,
    Schema,
)


class BaseSchema(Schema):
    class Meta:
        ordered = True


class NotFoundSchema(BaseSchema):
    detail = fields.Str(
        required=False,
        description='Not found.',
        example='Not found.'

    )
