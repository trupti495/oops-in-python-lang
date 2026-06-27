from b import b
from c import c

class d(b, c):

    def __init__(self, name, age, we):
        b.__init__(self, name, age)
        c.__init__(self, we)

    def mno(self):
        print("from d")


obj = d("trupti", 18, 35)
"""
obj.xyz()
obj.abc()
obj.pqr()
obj.mno()
"""