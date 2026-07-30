""" union of sets, unique element of the both"""

s1 = set()
s1.update(range(10))

s2 = set()
s2.update(range(5,15))

s1_union_s2 = s1 | s2 # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

"""intersection of two sets, common elements"""

s1_intersection_s2 = s1.intersection(s2)  # {5, 6, 7, 8, 9}

""" set difference, A - B , elements of A that are not present in B"""
s1_difference_s2 = s1.difference(s2) # {0, 1, 2, 3, 4}

"""symmetric difference, all elements that are present in one of the either
    not in both sets.
"""

s1_symmetric_difference_s2 = s1.symmetric_difference(s2)
print(s1_symmetric_difference_s2)


