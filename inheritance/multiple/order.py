from product import product
from payment import payment
class order(product,payment):
    def bill(self):
        qty=int(input("enter quantity :"))
        total=self.price*qty
        print(self.show_product())
        print("total=",total)

        print(self.pay(total))

obj=order("car",5000)
obj.bill()
