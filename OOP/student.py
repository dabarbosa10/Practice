class Student:

    #class variable
    category="student"
    def __init__(self,name):
        #instance variable
        self.name=name

    #Instance method 
    def hello(self):
        print(f"Hello my name is {self.name}")

    def name_len(self):
        print(len(self.name))

    @classmethod
    def info(cls):
        print(f"This is a method the class {cls.category}")
    

    @staticmethod
    def add(a,b):
        print(a+b)


student1=Student("John")
Student.add(2,3)
Student.info()
student1.hello()
student1.name_len()

