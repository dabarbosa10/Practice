class Circle:
    import numpy

    @staticmethod
    def area(r):
        return 3.1416*r*r
    
    @staticmethod
    def circumference(r):
        return 3.1416*2*r


a=Circle.area(10)
print(a)