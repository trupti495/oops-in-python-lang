# duck typing
#  This means Python does not check whether an object belongs to a specific class. 
#It only checks whether the object can perform the required action (has the required method).
class payment:
    def pay(self):
        pass
        print("payemnt process started")

class upi(payment):
    def pay(self):
        return"payment done by upi"
    
class gpay(payment):
    def pay(self):
        return"payemnt done by gpay"   
    
class payment_module:
    def payment_process(self,obj):
        print(obj.pay())

#u=upi()
#print(u.pay()) 

#g=gpay()
#print(g.pay())        

print("payment")
print("1.upi\n2.gpay\n3.card\n4.exit")
choice=int(input("enter your choice"))

match choice:
    case 1:
        obj=upi()
        #print(obj.pay())
    case 2:
        obj=gpay()
        #print(obj.pay())
    case 3:
        pass

    case 4:
        exit()

    case _:
        print("invalid choice")
#p=payment_module()
#p.payment_process(obj)

# duck typing
obj=[upi(),gpay()] 
for i in obj:
 print(i.pay())                     