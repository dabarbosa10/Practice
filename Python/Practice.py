prices=[100, 200, 300, 350, 450, 500]
new_list=list(filter(lambda x: x>300,prices))
print('--------------------')
print(new_list)
#Now let's apply the map function to the prices
new_prices=list(map(lambda x: x-x*0.1, prices))
print('--------------------')
print(new_prices)