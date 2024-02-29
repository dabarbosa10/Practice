#Creating a class 
class Vehicle:
    #creating a class attribute
    class_attribute="This is a vehicle class"
    #Creating a constructor 
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def display_info(self):
        print(f"Brand: {self.name}, color: {self.color} ")
    
    def class_method(cls):
        print("This is a class method")
        print(f"I can access the class attribute: {cls.class_attribute}")

    @staticmethod
    def static_method():
        print("I'm a static method, I cannot access anything")

class Car(Vehicle):
    def __init__(self, name, color,fuel_type):
        super().__init__(name,color)
        self.fuel_type=fuel_type

    def display_info(self):
        print(f"{self.name}, {self.color}, {self.fuel_type}")

#Create an Object
vehicle=Vehicle("Chevrolet", "Black")
vehicle.display_info()
print(f"vehicle brand is: {vehicle.name} and vehicle color is: {vehicle.color}")

##

car=Car("Mercedes Benz", "Blue","Gas")
car.display_info()
car.class_method()
car.static_method()

print(Vehicle.class_attribute)