#run time polymorphism
#Method overriding is achieved when a child class defines a method 
# with the same name as a method in the parent class. The child class 
#method is executed when called through the child object."
class payment:
    def pay(self):
        print("payemnt process started")

class upi(payment):
    def pay(self):
        return"payment done by upi"
    
class gpay(payment):
    def pay(self):
        return"payemnt done by gpay"
obj=upi()
obj.pay()

obj1=gpay()
obj1.pay()