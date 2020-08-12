from itertools import combinations as comb
from itertools import combinations_with_replacement as cwr

# where selection matters takes 2 arguments(both required) iterablr and r=no. of items to be selected

print(list(comb([1,2,3,4],r=1)))
print(list(comb([1,2,3,4],r=2))) # => doen't returns 1,1 2,2 3,3 4,4
print(list(comb([1,2,3,4],r=3)))
print(list(comb([1,2,3,4],r=4)))
print()
#CWR IS USED WHEN THERE CAN BE REPETITIONS => REPETITIONS ARE ALLOWED

print(list(cwr([1,2,3,4],r=2))) #=> also returns 1,1 2,2 3,3 4,4 
print('\n')
print(list(cwr([1,2,3,4],r=1)))
print('\n')
print(list(cwr([1,2,3,4],r=3)))
print('\n')
print(list(cwr([1,2,3,4],r=4)))
print('\n')


# Similar with other iterablesa