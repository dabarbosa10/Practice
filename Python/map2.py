nums=["1","2","3","4","5"]
new_ls=list(map(int,nums))
print(new_ls)

prices=[100,200,300,400,500]
ls1=list(map(lambda x: x<300,prices))
print(ls1)

ls2=list(map(lambda x: x-x*5/100, prices))
print(ls2)

names=['john', 'rob', 'mike']
Nnames=list(map(str.capitalize,names))
print(Nnames)