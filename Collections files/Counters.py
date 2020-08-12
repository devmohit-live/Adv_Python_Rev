'''
Sub class of dictionary that stores elements of an iterable as key and their count as their value
it returns the list  of dictionary (ordered) the key having the highest value will be at first position , 
the keys having the same value will be in lexographical order
the most common method give n most common elements ex n=2  will give top 2 elements that have occured most =>
returns list of tuples with (k,v) pattern

'''
from collections import Counter
s='Allahabad'
c=Counter(s)
print(c)
c1=Counter([1,2,1,1,1,1,1,2,2,2,1,2,3,5,6,4,9,0,9,9,0,5,6])
print(c1)
print('c.elemets will return an iterable k*v')
print(list(c.elements()))

print('Most Common method (helpful)')
print('n=2, gives top 2 most occured element', c.most_common(2))