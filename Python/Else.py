n=int(input('Enter numerator: '))
d=int(input('Enter denominator: '))

try:
    result=n/d
except ZeroDivisionError:
    print('Cannot divide a number by zero')
# if there is no exception
else:
    print(result)
#typically to close connections or files we use finally
#because it is executed no matter what
finally:
    print('It does not matter the exception :) ')