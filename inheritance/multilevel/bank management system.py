class bank:
    def __init__(self,bname,ifscode):
        self.bankname=bname
        self.ifsc=ifscode

    def display_bank(self):
        print("bank name:",self.bankname)  
        print("ifsc code:",self.ifsc)      

class account(bank):
    
    def __init__(self,holder,no,bname,ifscode):
        super().__init__(bname,ifscode)
        self.holder=holder
        self.no=no

    def display_account(self):
        super().display_bank()
        print("holder name:",self.holder)
        print("account no:",self.no)
        

class saving(account):

    def __init__(self,bal,fd,holder,no,bname,ifscode):
        super().__init__(holder,no,bname,ifscode)
        self.balance=bal
        self.fd=fd

    def display_saving(self):
        super().display_account()
        print(f"balance:{self.balance}\nFd:{self.fd}")
        

s1=saving(10000,500,"trupti",12345678,"bank of maharashtra","MAHB0000172")
  
s1.display_saving()




        
