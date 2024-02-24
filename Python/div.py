def division(a,b):
    try:
       result= a/b
    except ZeroDivisionError:
        print('We cannot divide by zero, try another one')
        return 0
    else:
        return result
    

if __name__=='__main__':
    a=int(input('Please enter numerator: '))
    b=int(input('Please enter denominator: '))
    print(division(a,b))
    