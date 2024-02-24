def function():
    counter =0
    while counter <=10:
        yield counter
        counter = counter+1

print(list(function()))

#list of even numbers
def funceven(quant):
    counter=0
    while counter<=quant:
        yield counter*2
        counter=counter+1
print(list(funceven(quant=10)))
    
#Another way of generate 
def funcood(x):
    for i in range(x):
        if i%2==1:
            yield i
print(list(funcood(10)))