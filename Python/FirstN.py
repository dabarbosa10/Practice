names=['John Doe', 'Alice Smith', 'Bob Ford']
new_n=list(map(lambda x: x.split()[0][0]+x.split()[1][0],names))
print('------With map------')
print(new_n)
print('-----Iterating------')
for name in names:
    print(name.split()[0][0]+name.split()[1][0])