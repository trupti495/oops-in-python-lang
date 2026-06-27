from p1 import p1
from p2 import p2
class p3(p1,p2):
    def pqr(self):
        print(" i am from p3")
    
    def call_p2_show(self):
        p2.show(self)

    def __init__(self,name,age):
        p1.__init__(self,name) # we are able to call constructor from their class name
        p2.__init__(self,age)    

obj=p3("trupti",20)
obj.xyz()
obj.abc()
obj.pqr()

# to call same method in p1 and p2 it call p1 method according 
# to the mro 
obj.show() # call only p1 show

# to call p2 method
obj.call_p2_show()

