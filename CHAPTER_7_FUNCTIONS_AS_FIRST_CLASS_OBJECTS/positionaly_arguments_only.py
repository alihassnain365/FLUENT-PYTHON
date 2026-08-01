# def greet(name):
#     """returns the name"""
#     print(f"Name is {name}")

# greet('Ali')
# # we could also call it keyword arguments
# greet(name='ali')

"""But what if we want a function never accepts the keyword arguemnts"""
def greet(name,/): # / is used to make the positional only def
    """returns the name"""
    print(f"Name is {name}")

greet('Ali')
# greet(name='Ali') # TypeError: greet() got some positional-only arguments passed as keyword arguments:'name'
