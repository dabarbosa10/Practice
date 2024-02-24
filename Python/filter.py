nums=[1,2,3,4,5,6,7,8,9]
even_nums=[]

def odd(x):
    if x%2==1:
        return x
    


odd_ls=list(filter(odd,nums))
odd_ls_lb=list(filter(lambda x: x%2==1,nums))
print('using lambda: --------------------------------------')
print(odd_ls_lb)
print('using definition: ----------------------------------')
print(odd_ls)

for num in nums:
    if num%2==0:
        even_nums.append(num)
print(even_nums)