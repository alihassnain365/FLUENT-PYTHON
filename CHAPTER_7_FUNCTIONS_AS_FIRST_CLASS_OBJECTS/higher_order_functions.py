"""Python functions are first class objects,  and they are higher order
    functions. A function is Higher Order , if it do the following one:
    i. takes an Argument as a function
    ii. returns a Function
"""

""" Sorting a list of words by length"""

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

"""sorted() is a higher order function, as it takes key= some function, 
    for example, we could pass any function at key =
"""


""" Sorting a list of words by their reversed spelling"""
def reverse(fruit:list)->list:
    """takes a list and returns its reverse order"""
    return fruit[::-1]

"""Now using this function and passing them as an argument
"""

print(sorted(fruits,key=reverse))
