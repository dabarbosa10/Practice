#String='Hello'
#rev_str=''.join(reversed(String))
#print(rev_str)
words=['Python', 'Java', 'JavaScript', 'C++']
new_ws=list(map(lambda word: word[::-1],words) )
print(new_ws)