from animal import animal
class dog(animal):
 
 def __init__(self):
    print("object created:")

 def __init__(self,name,we,colour):   
  self.colour=colour
  super().__init__(name,we)

 def display(self):
    super().greet()
    print("hello i am child")

obj=dog("cat",20,"black")
# to call parent class variable
print(obj.name)
print(obj.weight) 
print(obj.colour)

# to call parent class methods
obj.xyz()
obj.display()