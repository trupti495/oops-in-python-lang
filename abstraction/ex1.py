#need abc module and also abstract method to implement the abstraction
#abstract method need to override in the child classk
# normal method dont add any compulsion on child method
# not able create a abstract class 
from abc import ABC,abstractmethod
class a(ABC):
        def xyz(self):
            print("hello xyz")
        @abstractmethod
        def show(self):
              pass

class b(a):
      pass
      def show(self):
            print("hello i am abstract method") 
obj=b()
obj.xyz()
obj.show()            

