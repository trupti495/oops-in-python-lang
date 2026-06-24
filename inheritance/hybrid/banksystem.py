# real time example of multilevel deposite withdrawn and fd calculation
class bank:
    bankname="maharashtra"
    ifsc="mahb0000172"

    def display_bank(self):
        print("bank name:",self.bankname)  
        print("ifsc code:",self.ifsc)      

class account(bank):
    def get_account_info(self):
        
        self.hld=input("enter holder name:")
        self.no=int(input("enter account number:"))
        print("account created successfully")

    def display_account(self):
        super().display_bank()
        print("holder name:",self.hld)
        print("account no:",self.no)
        
class balance:
      bal=0
      
      def display_bal(self):
       print(" total balance:",self.bal)

class withdraw(balance):

    def get_withdraw(self):
     amount=float(input("enter amount you want to withraw:"))
    
     if amount>0:
        if balance.bal-amount>=2500:
            balance.bal=balance.bal-amount
            print("amount is successfully withdrawn !!!")
        else:
            print("not elligiable to withdrawn(need minimum 2500 balance)")

     else:
        print("account balance is zero !!!")        

class deposite(account,withdraw):

    def get_deposite(self):
     dep=float(input("enter amount to deposite"))
     balance.bal=balance.bal+dep
     print("amount added successfully !!!")   


d=deposite()
choice=0
while choice!=7 :
 print("---------\n1.bank detail\n2.create account\n3.view account\n4.withdraw\n5.deposite\n6.check balance\n7.exit")
 choice=int(input("enter your choice:"))
 
 match choice:
  case 1:
       d.display_bank()
  case 2:
       d.get_account_info()
  case 3:
       d.display_account()
  case 4:
       d.get_withdraw()
  case 5:
       d.get_deposite()
  case 6:
         d.display_bal() 
  case 7:
         print("exit successfully !!!")       
  case _:
         print(" invalid choice !!!")                      

      
       
       
       
           







        
