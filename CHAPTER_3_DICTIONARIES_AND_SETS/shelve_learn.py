"""Shelve :: But why """
# shelve is a built-in Python module that provides a persistent dictionary, 
# allowing you to store and retrieve Python objects using keys, just like a 
# normal dictionary, while automatically using pickle behind the scenes for 
# serialization. Although pickle can save almost any Python object, it works 
# with file objects, meaning you must manually open the file, load the entire 
# object, modify it, and save the entire object back again, even if you only 
# want to change one small piece of data. This becomes inconvenient when storing 
# many objects or when you need to access them individually. shelve solves this 
# by combining the flexibility of pickle with the convenience of a dictionary 
# interface, letting you store, retrieve, update, and delete objects by their 
# keys without manually handling the serialization process.

"""1. opening and storing in shelve"""

import shelve

class Fruit:
    """Models a fruit"""

    def __init__(self,name:str, calories:float):
        """Sets up fruit name and calories it contains"""
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        """shows the summary of fruit"""
        print(self.name,self.calories, sep=': ')



db = shelve.open('students_shelve') # now db is an open shelve
db['student1'] = {
    'name': 'Ali Hassnain',
    'discp':'Python developer',
    'source':'Fluent Python'
}

db['student2'] = {
    'name' : 'Abdullah Nadeem',
    'discp' :'dsa',
    'source':'UCP'
}


""" Now getting data back from that shelve"""

# print(db['student1'])
# print(db['student2'])

""" We could also access a specific value inside that shelf"""
# print(db['student1']['source'])



""" now storing the object in a shelve database"""
# this dictionary holds the object from the class fruit

fruit_object_dict = {
    'apple':Fruit('Apple',10),
    'banana':Fruit('Banana',20),
    'mango':Fruit('Mango',30)
}

""" Wr are storing these object in the shelve."""
# shelve uses pickle behind its working, as when we pickle
# we could handle only one complete object at a time, if we want
# to do change in any of one, we had to load the complete

""" like here if we want to change the calories of apple, we cant
    use pickle, becuase pickle would bring all the objects and we have 
    to seperate them and then do what ever we want
    . But shelve provide us this facility that we can change small elements
    inside our shelve, it uses pickle in its back"""

with shelve.open('fruit_shelve') as f_shelve:
    f_shelve.update(fruit_object_dict)
    # print(f_shelve['apple'])  "<__main__.Fruit object at 0x0000016EDD4E9A30>"
    

"""Now we have stored multiple objects in the shelve, sya we want to change the 
    calories of the banana to 1000 , 
"""

with shelve.open('fruit_shelve') as f_shelve:
    banana_new: Fruit = f_shelve.get('banana')

banana_new.calories = 1000

# banana_new.describe_fruit() # calories : 1000


""" now if we wnat to update the data in the shelf , we
    have to update the shelve.
"""

# shelve before updation
with shelve.open('fruit_shelve') as f_shelve:
    for shelf in f_shelve:
        f_shelve[shelf].describe_fruit()

""" OUTPUT

Apple: 10
Banana: 20
Mango: 30

"""

"""Now updating the shlve wiht updated banana"""

with shelve.open('fruit_shelve') as f_shelve:
    f_shelve.update({'banana':banana_new})


# now shelve after updation

with shelve.open('fruit_shelve') as f_shelve:
    for fruit_key in f_shelve:
        f_shelve[fruit_key].describe_fruit()

""" OUTPUT
Apple: 10
Banana: 1000
Mango: 30

"""


