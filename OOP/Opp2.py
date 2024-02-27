
''' def product_data():
    product_name=input('Enter name of the product: ')
    product_price=input('Enter price of the product: ')
    print(product_name)
    print(product_price)

product_data()'''

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    #Get
    def get_data(self):
        self.name=input('Enter name of the product: ')
        self.price=input('Enter price of the product: ')

    def put_data(self):
        print(self.name)
        print(self.price)

class DigitalProduct(Product):
    def __init__(self,link):
        self.link=link
    
    def get_link(self):
        self.link=input('Enter link of the product: ')
    
    def put_link(self):
        print(self.link)

eBook=DigitalProduct(" ")
eBook.get_data()
eBook.get_link()
eBook.put_data()
eBook.put_link()