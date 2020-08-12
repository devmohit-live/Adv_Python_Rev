from collections import deque
# A list like container woth fast append and pop on either end (Double ended queue)
d=deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.appendleft(4)
print(d)
print('pop',d.pop())
print('pop left',d.popleft())

# Supports count and extend as normal list container
d.extendleft([7,8,9])
print('Extend',d)
d.extend([1,2,1])
print('Extend left',d)
print('count:', d.count(1))

print('Remove fx removes only first occurance')
d.remove(1)
print(d)