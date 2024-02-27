class Product:
    quantity=200
    #constructor: initialize object
    def __init__(self,name,price):
        self.name=name #attribute1
        self.price=price #attribute2
    #another methods:
        
    def summer_discount(self,discount_percert):
        self.price=self.price-self.price*discount_percert


p1=Product("TShirt", 10)
print(p1.name)
print(p1.price)
p1.summer_discount(0.10)
print(p1.price)

#print('----------------------')
#p2=Product("laptop", "900")
#print(p2.name)
#print(p2.price)

#p1=Product()
#print(p1.quantity)