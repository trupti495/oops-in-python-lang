import random
import time

class insta:
    def __init__(self, username, pwd):
        self.username = username
        # private var
        self.__pwd = pwd
        self.__otp1 = None

    def verify_otp(self):
        otp2 = int(input("enter otp: "))

        if self.__otp1 == otp2:
            current_time = time.time()

            if current_time - self.otp_time <= 10:
                print("correct otp")
            else:
                print("OTP expired")
        else:
            print("wrong otp")

    def login(self, username, password):
        if self.username == username and self.__pwd == password:
            print("login successfull")

            otp = random.randint(1000, 9999)
            self.__otp1 = otp

            self.otp_time = time.time()   # added this line

            print("your otp:", self.__otp1)
            self.verify_otp()
        else:
            print("invalid credinational!!")


obj = insta("trupti", 1234)
obj.login("trupti", 1234)