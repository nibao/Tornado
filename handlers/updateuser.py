import tornado.web
from Tornado.db import get_cursor
import json

class UpdateUserHandler(tornado.web.RequestHandler):
    def post(self):
        if self.request.headers["Content-Type"].startswith("application/json"):
            body = self .request.body
            request_body = json.loads(body)

        oldinfo = request_body.get('old_username')
        newinfo = request_body.get('new_username')

        with get_cursor() as cursor:
            sql = 'UPDATE `t_users` SET `f_username` = %s WHERE `f_username` = %s'
            cursor.execute(sql,(newinfo,oldinfo))

