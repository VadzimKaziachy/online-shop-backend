from playhouse.shortcuts import model_to_dict

from base.handler import (
    BaseHandler,
)
from settings.constants import (
    HTTP_200_OK
)
from apps.products.schemas import (
    ProductSchema
)
from apps.products.models import (
    ProductModel
)


class ProductsHandler(BaseHandler):

    async def get(self, id):
        """
        ---
        tags: [categories]
        summary: Call for read list products by id category
        description: Request for return a list ProductModel.

        parameters:
            - in: path
              schema: IdParameter

        responses:
            200:
                description: return list ProductModel
                content:
                    application/json:
                        schema:
                            ProductSchema
            404:
                description: return 404 error
                content:
                    application/json:
                        schema:
                            NotFoundSchema

        """
        products = await self.application.objects.execute(ProductModel.select().filter(category=id))
        self.json_response(
            status=HTTP_200_OK,
            body=[model_to_dict(obj, only=(ProductModel.id, ProductModel.name)) for obj in products]
        )
