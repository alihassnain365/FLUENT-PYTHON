""".keys(), .items(), .values() these dictionary operatoin returns a dictionary view
    It is a read only projection mean we can only read it not update or do change of it.
"""

person = dict(name='Ali Hassnain', age = 22, address = 'ghanian ghazi', friends =['ahsan','sadi','sheki','mango'])


""" grab the list of all the keys of the dictionary"""
person_keys = person.keys()



""" grab all the values of the each key of the dictionary"""

person_values = person.values()

"""these views are ieteable"""

for key in person_keys:
    print(key)

""" we could also implement reverse , len etc on these views"""


reversed_dict_view = reversed(person_keys) 
# it would create a ieterable object 
print(type(reversed_dict_view)) # dict_reversekeyiterator

""" this object is ietarable"""
for key in reversed_dict_view:
    print(key)

"""but we cannot use the [] indexing in views object"""

# print(person_keys[0])  "TypeError: 'dict_keys' object is not subscriptable"


""" these view are auto updated, if we change in the original dictionary
    it would reflect in the views as well"""


person.update({'ismarried':True})

""" now this updation would be seen in the previously created views"""

print(person_keys) # ismarried would appear 









