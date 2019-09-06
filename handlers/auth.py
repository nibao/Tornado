import time
import hashlib
import jwt
from Tornado.db import get_cursor
from Tornado.handlers.base import BaseHandler
import json

def get_token():
    access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImVjaG8xMTEiLCJpYXQiOjE1Njc2NjEwOTQuMzY3LCJqdGkiOiJlODg5MmVlMS1iN2QwLTQzZTgtODg0Mi1kODk5M2FkYmYyODIiLCJleHAiOjE1Njc2NjQ3MTF9.DVg9xcmIc2VaQoP03YvwO355bbqq5g5EEFeZK1a7Ydo'
    #返回生成token给result
    return {
        'access_token':access_token
    }

class NewToken(BaseHandler):
    def post(self):
        if self.request.headers["Content-Type"].startswith("application/json"):
            body = self.request.body
            request_body = json.loads(body)
        username = request_body.get('username')
        password = request_body.get('password')

        with get_cursor() as cursor:
            sql = 'SELECT * FROM `t_users`WHERE `f_username` = %s'

        cursor.execute(sql,(username,))
        user_info = cursor.fetchone()
        #校验用户密码是否正确
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        pwd_hash = sha256.digest()
        print (pwd_hash)
        if pwd_hash != user_info[2]:
            print ('Error!!!')
        #密码通过校验，生成token
        '''
        result格式：{'access_token':xxxx.yyyy.zzz,'token_type':'bearer'}
        '''
        result = get_token()
        self.write_result(result)



