import json

from playhouse.shortcuts import model_to_dict

from ..schemas import (
    CategoryCreateSchema,
)
from ..models import (
    CategoryModel,
)
from base.handler import (
    BaseHandler,
)
from settings.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)


class CategoriesHandler(BaseHandler):

    async def get(self):
        """
        ---
        tags: [categories]
        summary: Call for read list categories
        description: Request for return a list CategoryModel.

        responses:
            200:
              description: list of categories
              content:
                application/json:
                    schema:
                        type: array
                        items:
                            CategorySchema


        """
        categories = await self.application.objects.execute(CategoryModel.select())

        self.json_response(
            status=HTTP_200_OK,
            body=[model_to_dict(obj, only=(CategoryModel.id, CategoryModel.name)) for obj in categories]
        )

    async def post(self):
        """
        ---
        tags: [categories]
        summary: Call for create category
        description: Request for created new category.

        requestBody:
            description: New car brand data
            required: True
            content:
                application/json:
                    schema:
                        CategoryCreateSchema

        responses:
            201:
                description: return object CategoryModel
                content:
                    application/json:
                        schema:
                            CategorySchema

            400:
                description: return 400 error
                content:
                    application/json:
                        schema:
                            BadRequestSchema

        """
        body = json.loads(self.request.body)

        if validation_errors := CategoryCreateSchema().validate(body):
            self.json_response(status=HTTP_400_BAD_REQUEST, body={'errors': validation_errors})
        else:
            category = await self.application.objects.create(CategoryModel, name=body.get('name'))

            self.json_response(status=HTTP_201_CREATED, body=model_to_dict(category))
