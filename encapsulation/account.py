# wrapping up of a data in single cell in encapsulation we majaroly use the private 
# data member and acess it in the public member

class Account:
    def __init__(self, bal):
        self.__bal = bal      # private variable

    def get_bal(self):
        return self.__bal

    def set_bal(self, amt):
        self.__bal = amt # acessing the private variable in private method
        print("Balance updated")

    def __private_method(self): #private method
        print("Hello, I am private")

    def acess_pm(self): # acessing the private variable in private method
        self.__private_method()
    
    def __withdraw(self):
        dep=int(input("enter amount to withdraw"))
        if self.__bal>dep:
            self.__bal=self.__bal-dep
            return f"{dep} amount is debited \nbalance={self.__bal}"  
        else:
            return"Insufficient bank balance"
        
    def acess_withdraw(self):
        return self.__withdraw()  

    def __deposit(self):
        amt=int(input("enter amount to deposite"))
        if amt>0:
         self.__bal += amt
         return "Amount deposited successfully"

    # Public method
    def deposit_money(self):
        self.__deposit() 

obj = Account(500)
"""
# Access private member through public methods
print(obj.get_bal())
"""
#obj.set_bal(5000)
print(obj.get_bal())

obj.acess_pm()

# acess withdraw
print(obj.acess_withdraw())

#acess deposite
print(obj.deposit_money())
