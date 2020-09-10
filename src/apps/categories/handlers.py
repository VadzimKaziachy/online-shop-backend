import json
from . import schemas
from tornado.web import RequestHandler

from .models import (
    CategoryModel,
)


class CategoriesHandler(RequestHandler):
    SUPPORTED_METHODS = ("GET", "HEAD", "POST")

    async def get(self):
        """
        ---
        tags:
        - Categories
        summary: Call for read list categories
        description: Request for return a list CategoryModel.
        schema:
            type: array
            items: 'CategoryModel'
        produces:
        - application/json
        responses:
            200:
              description: list of categories


        """
        categories = await self.application.objects.execute(CategoryModel.select())

        self.write(json.dumps([{'id': obj.id, 'name': obj.name} for obj in categories]))

    async def post(self):
        """
        ---
        tags:
        - Categories
        summary: Call for create category
        description: Request for created new category.
        produces:
        - application/json
        responses:
            200:
              description: return object CategoryModel
        """
        body = json.loads(self.request.body)

        category = await self.application.objects.create(CategoryModel, name=body.get('name'))

        self.write({'id': category.id, 'name': category.name})
