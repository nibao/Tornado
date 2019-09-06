import tornado.web
from Tornado.db import get_cursor
import pdb

class SearchUserHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username')

        with get_cursor() as cursor:
            sql = "SELECT * FROM `t_users` WHERE `f_username` = %s"
            cursor.execute(sql,(username,))
            result = cursor.fetchall()
            print (result)


