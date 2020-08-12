from itertools import permutations as perm
# where arrangement is important
# takes iterable, can also take r, where r is no of items i per tuple to be comsidered in an arrangment

print(list(perm(range(3))))
print()
print(list(perm([1,2,3,4])))
print()
print(list(perm([1,2,3,4],2)))
print()
print(list(perm('abc')))
print()