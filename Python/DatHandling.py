file=open('data.txt','r')
#content=file.read(10) # Reading only 10 bytes
cont=file.readline()# Read only first line
print(cont)
file.close()