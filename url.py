from Tornado.handlers import adduser,deleteuser,updateuser,searchuser,auth

URL = [
    (r'/add', adduser.AddUserHandler),
    (r'/delete',deleteuser.DeleteUserHandler),
    (r'/update',updateuser.UpdateUserHandler),
    (r'/search',searchuser.SearchUserHandler),
    (r'/auth',auth.NewToken)
]