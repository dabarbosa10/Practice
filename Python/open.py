with open('names.txt','r') as file:
    lines = file.readlines()    


print(lines) # here we print the list

for line in lines:
    print(line.strip())
