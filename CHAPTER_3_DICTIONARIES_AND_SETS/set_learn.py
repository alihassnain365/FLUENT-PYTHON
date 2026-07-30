""" sets stores the unique values
    1. so the main usecase is removing duplication
"""
l = [1,1,2,2,3,3,4,4]
set_l = set(l)
print(set_l)

"""if sets or ordered"""
print(set_l)

""" set type is not hashable , so basically it couldnt be used as 
    key in dictionary. But the frozen set is hashable so it could 
    be used as the keys in the dictionaries.
"""
# hash(set_l) "TypeError: unhashable type: 'set'"

""" difference between a frozen set and a simple set"""
frozen_set = frozenset((1,2,3,4,5,6,7,8,9))
simple_set = set((1,2,3,4,5,6,7,8,9))

# could we add in both 
simple_set.add(10) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# frozen_set.add(11)  AttributeError: 'frozenset' object has no attribute 'add'

# could we delete from them
print(simple_set.pop()) # pop removes the first element from the set and returns
 # we cant pop from the frozen set








