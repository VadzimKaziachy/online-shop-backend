from tornado.web import url

from .handlers import (
    CategoryHandler,
    CategoriesHandler,
)

routes = [
    url(r'/categories', CategoriesHandler),
    url(r'/categories/(?P<id>[0-9]+)$', CategoryHandler)
]
