import json

from peewee import DoesNotExist
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
    HTTP_204_NO_CONTENT,

    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,

    HTTP_404_NOt_FOUND_BODY,
)


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

            404:
              description: object not found
              content:
                application/json:
                    schema:
                        NotFoundSchema

        """
        try:
            await self.application.objects.delete(CategoryModel.get(id=id))

            self.json_response(status=HTTP_204_NO_CONTENT, body={})
        except DoesNotExist:

            self.json_response(status=HTTP_404_NOT_FOUND, body=HTTP_404_NOt_FOUND_BODY)

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
            400:
                description: return 400 error
                content:
                    application/json:
                        schema:
                            BadRequestSchema
            404:
                description: return 404 error
                content:
                    application/json:
                        schema:
                            NotFoundSchema
        """
        body = json.loads(self.request.body)

        if validation_errors := CategoryCreateSchema().validate(body):
            self.json_response(status=HTTP_400_BAD_REQUEST, body={'errors': validation_errors})
        else:
            try:
                body = json.loads(self.request.body)

                category = await self.application.objects.get(CategoryModel, id=id)
                category.name = body.get('name')

                await self.application.objects.update(category)

                self.json_response(status=HTTP_200_OK, body=model_to_dict(category))
            except DoesNotExist:

                self.json_response(status=HTTP_404_NOT_FOUND, body=HTTP_404_NOt_FOUND_BODY)
