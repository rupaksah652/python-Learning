#google example
class SecurityError(Exception):

    def __init__(self,message):
        print(message)

    def logout(self):
        print('logout')

class google:

    def __init__(self,name,email,password,device):
        self.name=name 
        self.email=email 
        self.password=password
        self.device=device

    def login(self,email,password,device):
        if device!=self.device:
            raise SecurityError('u gone bro')
        if email==self.email and password==password:
            print('welcome')
        else:
            print('login error')

obj=google('nitish','nitish@gmail.com','1234','android')
try:
    obj.login('nitish@gmail.com','1234','window')
except SecurityError as e:
    e.logout()
else:
    print(obj.name)
finally:
    print('databse connected successfully')