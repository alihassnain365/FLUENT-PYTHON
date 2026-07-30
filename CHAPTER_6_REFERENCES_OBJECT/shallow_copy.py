l1 = [1,[2,3],4]
l2 = l1.copy()

l1[1].append(100)
"""
i have did the change in l1, but it would also reflect in l2.
Becuase, l1 contains a mutable refrence of list [2,3] , so wheln
l1.copy() runs it creates a refrence that has all the new copies of
immutable types like 1,2 and 4, but when it sees a list, it share the 
refrence of that list in both l1 and l2
"""

print(l1)
print(l2)


"""Python does this intentionally, imagine you have a very big list , which contains
many lists inside, so if we try copying the all contents then it would take some time
and consume memory along with computation.
But if we want to really do a deep copy. Then we have to use the Copy librarry"""

from copy import deepcopy

l3 = deepcopy(l1)

l1[1].append(1200)
print(l1) # they are not same
print(l3)

