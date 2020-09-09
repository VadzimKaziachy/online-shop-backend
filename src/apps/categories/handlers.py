from tornado.web import RequestHandler

from .models import (
    CategoryModel,
)


class CategoryHandler(RequestHandler):
    async def get(self):
        categories = await self.application.objects.execute(CategoryModel.select())

        self.write(str([{'id': obj.id, 'name': obj.name} for obj in categories]))
