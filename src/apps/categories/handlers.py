import json

from peewee import DoesNotExist

from . import schemas
from .models import (
    CategoryModel,
)
from base.handler import (
    BaseHandler,
)
from settings.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)


class CategoriesHandler(BaseHandler):
    SUPPORTED_METHODS = ("GET", "HEAD", "POST")

    async def get(self):
        """
        ---
        tags: [Categories]
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

        self.json_response(HTTP_200_OK, [{'id': obj.id, 'name': obj.name} for obj in categories])

    async def post(self):
        """
        ---
        tags: [Categories]
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

        """
        body = json.loads(self.request.body)

        category = await self.application.objects.create(CategoryModel, name=body.get('name'))

        self.json_response(HTTP_201_CREATED, {'id': category.id, 'name': category.name, 'created': category.created})


class CategoryHandler(BaseHandler):
    SUPPORTED_METHODS = ("DELETE", "PATCH")

    async def delete(self, id):
        """
        ---
        tags: [Categories]
        summary: Call for delete category
        description: Request for created new category.

        parameters:
        - in: path
          schema: GistParameter

        responses:
            204:
              description: return object CategoryModel
              content:
                application/json:
                    schema:
                        CategorySchema
            404:
              description: object not found
              content:
                application/json:
                    schema:
                        NotFoundSchema

        """
        try:
            await self.application.objects.delete(CategoryModel.get(id=id))

            self.json_response(HTTP_204_NO_CONTENT, {})
        except DoesNotExist:

            self.json_response(HTTP_404_NOT_FOUND, {'detail': 'Not found.'})
