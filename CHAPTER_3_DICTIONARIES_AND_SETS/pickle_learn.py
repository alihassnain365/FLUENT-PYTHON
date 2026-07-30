"""
pickle is a built-in Python module that lets you save Python objects to a file
and load them back later. Think of it like taking a snapshot of an object
(such as a list, dictionary, or custom class instance) and storing that snapshot 
on your computer. This process of converting an object into a byte stream is called 
pickling (serialization), and restoring it back into a Python object is called 
unpickling (deserialization). For example, if your program creates a list of
 student records, you can pickle that list to a file, close the program, and 
 later unpickle the file to get the exact same list back without recreating it 
 manually. It is important to remember that pickle files should only be loaded 
 from trusted sources, because loading a malicious pickle file can execute 
 harmful code.

"""



""" Why should we use Pickle, as we could store data in .txt or .json """
# Imagine you have a Python dictionary, a custom class object, or even a machine
# learning model. With pickle, you can save it with one command and load it back 
# later in the same state, including its data types and object structure. JSON, 
# on the other hand, can only store basic data types like strings, numbers, lists, 
# dictionaries, booleans, and null. If you try to save a custom Python object or a 
# complex data structure, JSON will raise an error unless you manually convert it 
# into a JSON-friendly format. Plain text is even more limited because it only stores 
# characters, so you must manually decide how to format the data and later write code 
# to parse it back.

import json
import pickle
""" 1. saving object with .json"""
    # lets create a basic class
class Fruit:
    """Models a fruit"""

    def __init__(self,name:str, calories:float):
        """Sets up fruit name and calories it contains"""
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        """shows the summary of fruit"""
        print(self.name,self.calories, sep=': ')


""" 1.1: creating the instance of the class and then saving it"""

apple_fruit = Fruit('Apple',100.45)
     # now going to save that instance
with open('apple.json','w') as apple_file:
    data = dict(name = apple_fruit.name, calories = apple_fruit.calories)
    json.dump(data, apple_file)

""" ans same we would open and get the data from this and then 
    we would try to assign to the objecc and it is a mess, so to 
    avoid that python has pickle, it could store object directly 
    into bytestream etc. and you could get back whenver you want.
"""

"""2. saving with pickle"""

# banana_fruit = Fruit('banana',100.50)
# with open('banana.pickle','wb') as banana_file:
#     pickle.dump(banana_fruit, banana_file)
#     # Wallah : object is saved in the file

"""Now if i completely destroy the first object , or 
    use could use it in another program as well, 
    say  i am commenting the banana fruit object
    as we have stored it in and now we would load back it
    without creating the new one.
"""

with open('banana.pickle','rb') as banana_file:
    banana_new: Fruit = pickle.load(banana_file)

banana_new.describe_fruit()

