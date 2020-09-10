import peewee_async
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.httpserver import HTTPServer
from tornado_swagger.setup import setup_swagger

from settings.urls import routes
from settings.database import DATABASE

define('port', default=8000, help='port to listen on')


class OnlineShopBackend(Application):
    def __init__(self):
        setup_swagger(
            routes,
            swagger_url='/swagger',
            api_base_url='/',
            api_version='1.0.0',
            title='Online-shop API',
            schemes=['http']
        )
        self.objects = peewee_async.Manager(DATABASE)
        super(OnlineShopBackend, self).__init__(routes, **dict())


def main():
    server = HTTPServer(OnlineShopBackend())
    server.listen(options.port)

    IOLoop.current().start()


if __name__ == '__main__':
    main()
