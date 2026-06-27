# authentication process
#create a diffrent login for the admin and user
from abc import ABC,abstractmethod

class login(ABC):
    @abstractmethod
    def check_credentials(self):
        pass

class user(login):
   def __init__(self,admin,pwd):
       self.admin=admin
       self.pwd=pwd

   def check_credentials(self):
     admin1=input("enter username:")
     passw1=input("enter  password")
     if self.admin==admin1 and self.pwd==passw1:
        print("user successfully login")
     else:
        print("invalid credentials")   
      
class admin_log(login):
    
    def __init__(self,admin,pwd):
       self.admin=admin
       self.pwd=pwd

    def check_credentials(self):
     admin1=input("inter admin id:")
     passw1=input("enter admin password")
     if self.admin==admin1 and self.pwd==passw1:
        print("admin successfully login")

     else:
        print("invalid credentials")   

print("*** LOGIN SYSTEM ***")
print("1.user\n2.admin\n3.exit")
choice=int(input("enter your choice"))

match choice:
   case 1:
      a1=user("user","12345")
      a1.check_credentials()
   case 2:
      b1=admin_log("242102","1234")
      b1.check_credentials()
   case 3:
      exit()
   case _:
      print("invalid choice")
           
      