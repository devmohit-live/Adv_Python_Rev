'''
here we can give an initial value to dictionary, we can to the same with normal dictionary using setdefault() method too but it is fast,
also here we can give the datatype as default value ex d(list) nad the values will support the opration of that partivular datatype, ex:
d['mohit'].append()
defauldict() => takes one parameeter it can be a lambda function too
'''
from collections import defaultdict
d=defaultdict(int)
d['name']='Mohit'
print('Accessing the value of the key that doesnt exists (defaultdict(int)) d[hello] : ', d['hello'])

d=defaultdict(lambda:"String returned by lambda function")

# d=defaultdict("hello") => value can't be directly assigned as we do in setDefault()

print("d=defaultdict(lambda:'String returned by lambda function') as d=defaultdict('hello') value can't be directly assigned")
print('d[hello] : ',d['hello'])

d=defaultdict(list)
s=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
for k,v in s:
    d[k].append(v)

print(d)