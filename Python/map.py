numbers=[1,2,3,4,5]

def xpon(x):
    return x*3

for i in numbers:
    print(xpon(i))

new_list= list(map(xpon,numbers))
print(new_list) 

