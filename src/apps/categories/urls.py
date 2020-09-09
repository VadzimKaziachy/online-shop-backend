from .handlers import (
    CategoryHandler,
)


routes = [
    (r'/', CategoryHandler),
]