import tornado.web
from Tornado.db import get_cursor

class DeleteUserHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username')

        with get_cursor() as cursor:
            sql = 'DELETE FROM `t_users` WHERE `f_username` = %s'
            cursor.execute(sql,(username))