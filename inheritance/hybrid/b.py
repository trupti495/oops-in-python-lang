from a import a
class b(a):
    def abc(self):
        print("from b")

    def __init__(self,name,age):
        self.age=age
        print("age=",self.age) 
        a.__init__(self, name)   # instead of super()