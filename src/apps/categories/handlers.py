import json

from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict

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
            data=[model_to_dict(obj, only=(CategoryModel.id, CategoryModel.name)) for obj in categories]
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

        """
        body = json.loads(self.request.body)

        category = await self.application.objects.create(CategoryModel, name=body.get('name'))

        self.json_response(status=HTTP_201_CREATED, data=model_to_dict(category))


class CategoryHandler(BaseHandler):

    async def delete(self, id):
        """
        ---
        tags: [categories]
        summary: Call for delete category
        description: Request for delete category.

        parameters:
        - in: path
          schema: IdParameter

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

            self.json_response(status=HTTP_204_NO_CONTENT, data={})
        except DoesNotExist:

            self.json_response(status=HTTP_404_NOT_FOUND, data={'detail': 'Not found.'})

    async def patch(self, id):
        """
        ---
        tags: [categories]
        summary: Call for change category
        description: Request for change category

        parameters:
            - in: path
              schema: IdParameter

        requestBody:
            description: category
            required: True
            content:
                application/json:
                    schema:
                        CategoryCreateSchema

        responses:
            200:
                description: return change object category
                content:
                    application/json:
                        schema:
                            CategorySchema
        """
        try:
            body = json.loads(self.request.body)

            category = await self.application.objects.get(CategoryModel, id=id)
            category.name = body.get('name')

            await self.application.objects.update(category)

            self.json_response(status=HTTP_200_OK, data=model_to_dict(category))
        except DoesNotExist:

            self.json_response(status=HTTP_404_NOT_FOUND, data={'detail': 'Not found.'})
