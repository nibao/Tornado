
import uuid
import hashlib

import tornado.web
from Tornado.db import get_cursor

def pwd_hash(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

class AddUserHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        
        #将密码加密
        pwd = pwd_hash(password)
        #使用内置库，生成唯一ID,生成基于随机数的散列值
        uid = uuid.uuid4()

        with get_cursor() as cursor:
            sql = """
                INSERT INTO `t_users` 
                (`f_id`, `f_username`, `f_password`) 
                VALUES (%s,%s,%s)
            """
            cursor.execute(sql,(uid.int,username,pwd))

