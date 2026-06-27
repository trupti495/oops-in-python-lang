# method overloading means the same method name but diffrent argument 
# in python 100 per polymorphism is not acheive 

class demo:
    
    def add(self,a,b,c=100):
        print("addition=",(a+b+c))
d1=demo()
d1.add(10,20)
d1.add(10,20,30)        