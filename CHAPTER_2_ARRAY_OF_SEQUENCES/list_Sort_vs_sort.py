fruit = ['grapes','guava','orange','kiwi','apple']
# print(fruit)
# fruit.sort()
# print(fruit)

""" in python there is a convention that the 
    functions that returns NONE they changes the 
    original arguments like list or tuple or whatever
    it is.
    While the returning functions ceate a copy of it and
    do the working and returns the new one"""

print(sorted(fruit)) # it returns the new list
print(fruit)

print(sorted(fruit,reverse=True))

print(sorted(fruit,key=len))
