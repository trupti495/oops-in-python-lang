# not 100 per polymorphism acheive 
#giving  special meaning to an operator for user defined object

class student:

    def __init__(self,marks):
        self.marks=marks

    def __add__(self,other):
        return self.marks+other.marks
s1=student(50)
s2=student(60)
print(s1+s2)