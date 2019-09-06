
import tornado.web
import json


class BaseHandler(tornado.web.RequestHandler):
    def write_result(self, data: dict, status_code = 200):
        """返回API调用结果
        """
        self.set_status(status_code)
        self.set_header('Content_Type', "application/json; charset=UTF-8")
        self.write(json.dumps(data, indent=4))
