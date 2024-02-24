#Syntax error is a gramatical error.
# For example in defining a function we can have the following syntax errors:
# deff function(): or def function() are consider as syntax errors.
########------------
#-----------------------Logical errors--------------------------
# def add(a,b):
#   return a*b
# print(add(2,5))
# we expected 7 but instead we obtain 10
#--------------------------------------------------------------
n=int(input('Enter numerator: '))
d=int(input('Enter denominator: '))
result=0
try:
    result=n/d
except ZeroDivisionError:
    print('Cannot divide a number by zero')
print(result)