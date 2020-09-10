from tornado.web import url

from .handlers import (
    CategoriesHandler,
)


routes = [
    url(r'/categories', CategoriesHandler),
]