import json
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    """
    Application base handler
    """

    def json_response(self, status: int, body: dict or list):
        """
        Helper method for sending response containing json data
        """
        self.set_header("Content-Type", "application/json")
        self.set_status(status)
        if body:
            self.write(json.dumps(body, default=str))
        self.finish()
