# Keeps track of keys order (order in which the key,values are added)
from collections import OrderedDict
od = OrderedDict()
normal_dict = {}
od['Name'] = 'Mohit'
od['Branch'] = 'IT'
od['Year'] = 3
od['City'] = 'xyz'

od2=OrderedDict()
od2['Year'] = 3
od2['City'] = 'xyz'
od2['Name'] = 'Mohit'
od2['Branch'] = 'IT'
normal_dict['Name'] = 'Mohit'
normal_dict['Branch'] = 'IT'
normal_dict['Year'] = 3
normal_dict['City'] = 'xyz'

nd = {}

nd['Branch'] = 'IT'
nd['Year'] = 3
nd['City'] = 'xyz'
nd['Name'] = 'Mohit'

# //passing the normal dictionary to OrderedDict doesn't makes it ordered, since the passed dictionary values will be like city,name,branch and year only
# that is OrderedDict(normal_dict) doesn't help you


if __name__ == "__main__":
    print('Order dict ', od)
    print('Normal dict ', normal_dict)
    print('Printing Keys::')
    # since it is a special case of dictionary all the proprties and  fuctions can be applied to od too
    print(od.keys())
    print(normal_dict.keys())

    print("Comaprison between them == ")
    print("nd==normal_dict (two dict having same kv in different order)",
          normal_dict == nd)
    print("od==od2 (two ordereddict having same kv in different order)",
          od2 == od)
    print("od==normal_dict will always be true having same set of k,v", normal_dict == od2)
