# has a
# one class object is enject in the parent class
class engine:
 
 def __init__ (self,chessno,hopow):
  self.chessno=chessno
  self.hopow=hopow

 def display_engine(self):
  print("****** ENGINE INFO ******")  
  print("chess number :",self.chessno)
  print("horse power :",self.hopow)


class car:
 def __init__ (self,model,price):
  self.model=model
  self.price=price
  # engine object inserted
  self.e1=engine(1234,500)

 def display_car(self):
   c1.e1.display_engine()
   print("******car info*******")
   print("name:",self.model)
   print("price :",self.price)

c1=car("bmw","1cr")
c1.display_car()


  
