# is a
# like normal inheritaance
class animal:
    type="animaltype"
    def __init__(self):
     print("default constructor from animal!!!")

    def __init__(self,name,we):
     self.name=name
     self.weight=we

    def xyz(self):
     print(" hello i am from parent class")

    def greet(self):
     print("hello i am animal")        
