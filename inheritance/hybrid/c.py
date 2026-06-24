from a import a
class c(a):
    def pqr(self):
        print("from c")

    def __init__(self,name,we):
        self.we=we
        print("weight=",self.we)
        a.__init__(self, name)   # instead of super()  