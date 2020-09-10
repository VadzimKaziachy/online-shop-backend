from tornado_swagger.model import register_swagger_model


@register_swagger_model
class CategoryModel:
    """
    ---
    type: object
    description: CategoryModel model representation
    properties:
        id:
            type: integer
            format: int64
        name:
            type: string
    """