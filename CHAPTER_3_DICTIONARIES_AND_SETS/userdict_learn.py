"""
Python supports a dictionary like a container called UserDict present in the
collections module. This class acts as a wrapper class around the dictionary 
objects. This class is useful when one wants to create a dictionary of their 
own with some modified functionality or with some new functionality. It can be 
considered as a way of adding new behaviors to the dictionary. This class takes 
a dictionary instance as an argument and simulates a dictionary that
 is kept in a regular dictionary. The dictionary is accessible by the data 
 attribute of this class.

"""

from collections import UserDict

""" 1. Create a dictionary that behaves exactly like a normal dictionary. """
class MyDict(UserDict):
    """Models the behaviour of the dictionary"""
    pass

custom_dict = MyDict(name='ali',age = 12)

# print(type(custom_dict)) "<class '__main__.MyDict'>"
# print(custom_dict) "{'name': 'ali', 'age': 12}"

"""Exercise 2 — Print Whenever an Item is Added :{xx Item added}"""

class CustomPrintDict(UserDict):
    """Display message when the item is added to this dictionary"""
    def __setitem__(self, key, item):
        print(f"Adding {key} = {item}")
        return super().__setitem__(key, item)

print_dict = CustomPrintDict(name='ali hassnain', favourite_character = 11)
"""                 OUTPUT :
Adding name = ali hassnain
Adding favourite_character = 11

"""


"""Exercise 3 — Only Allow String Keys"""

class StringKeyDict(UserDict):
    """Models dictionary with extra feature of allowing string keys only"""
    def __setitem__(self, key, item):
        if not isinstance(key,str):
            raise TypeError('Key must be string')
        return super().__setitem__(key, item)

# mystring_key = StringKeyDict(1='ali') # error



"""Exercise 3 : Automatically convert key to lowercase"""

class LowerKeysDict(UserDict):
    """Models dictionary with feat. Lower keys automatically"""
    def __setitem__(self, key, item):
        key = key.lower()
        return super().__setitem__(key, item)

lower_keys = LowerKeysDict(NAME = 'ali')






