import swagger_ui
import peewee_async

from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.httpserver import HTTPServer

from settings.urls import routes
from settings.base import SWAGGER_API_OUTPUT_FILE
from settings.swagger import generate_swagger_file
from settings.database import DATABASE

define('port', default=8000, help='port to listen on')


class OnlineShopBackend(Application):
    def __init__(self):
        self.objects = peewee_async.Manager(DATABASE)
        super(OnlineShopBackend, self).__init__(routes, **dict())

        self._init_swagger()

    def _init_swagger(self):
        generate_swagger_file(handlers=routes, file_location=SWAGGER_API_OUTPUT_FILE)
        swagger_ui.tornado_api_doc(
            self,
            config_path=SWAGGER_API_OUTPUT_FILE,
            url_prefix='/swagger.html',
            title='Online-shop API',
        )


def main():
    server = HTTPServer(OnlineShopBackend())
    server.listen(options.port)

    IOLoop.current().start()


if __name__ == '__main__':
    main()
