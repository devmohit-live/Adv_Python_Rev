from itertools import product
# returns cartesian product in tuple form 
# useful in polynomial equations type question
# takes iterables as an arguments => can also take repeat=n n defines the power ex for n=2 => (1,2,3)^2 =>[1,2,3]x[1,2,3]
print(list(product([1,2,3],[4,5,6])))
print(list(product([1,2,3],repeat=2)))

