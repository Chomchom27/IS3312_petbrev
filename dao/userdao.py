from model.models import User

class UserDAO:
    def __init__(self):
        self.users=[User(1,'administrator','admin@admin.com','password','administrator'),
                    User(2,'customer','cust@cust.com','password','customer')]


    def getuser(self,user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user

    def getuserbyemail(self,email):
        for user in self.users:
            if user.email == email:
                return user

    def getuserbyusername(self,username):
        for user in self.users:
            if user.username == username:
                return user




if __name__ == '__main__':
    udao=UserDAO()
    print(udao.getuser(1))
    print(udao.getuser(2))