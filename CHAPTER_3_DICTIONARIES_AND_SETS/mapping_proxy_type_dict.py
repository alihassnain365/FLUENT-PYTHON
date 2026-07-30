"""Dictionaries are mutable, we could add or delete from them, 
    so to creat a readonly dictionary we use another way of
    MappingProxyType    
"""


changable_dict = dict(name='ali')
changable_dict.update({'age':12})
# print(changable_dict)  "{'name': 'ali', 'age': 12}"

from types import MappingProxyType

unchangeable_dict = MappingProxyType(changable_dict)
# unchangeable_dict['age'] = 100 "TypeError: 'mappingproxy' object does not support item assignment"
# print(unchangeable_dict) "{'name': 'ali', 'age': 12}"

"""Here is a twist."""
changable_dict['age'] = 100
# we havent changed the unchangeable_Dict
 
# print(changable_dict) "{'name': 'ali', 'age': 100}"
# print(unchangeable_dict) "{'name': 'ali', 'age': 100}"

"""Unchangeable_dict is syncing the changes in the changeable_dict
    it is becasue that MappingProxyType never creates the copy of the 
    provided dict , while it creates a read only view of that dict.
"""
"""So that the owner could do the changes in the dictionary, he uses the original
    dictionary , while the other user would use the Unchageable_view so that they 
    could not change the data.So that we could maintain the data safety
"""




