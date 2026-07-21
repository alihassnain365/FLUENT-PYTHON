# colors = ['red','blue']
# sizes = ['s','m','l']

# shirts_pairs = ((color,size) for color in colors 
#                             for size in sizes)
# print(shirts_pairs)
# for pair in shirts_pairs:
#     print(pair)

# for pair in shirts_pairs:
#     print(pair)



def add(x, y):
    """Added two numbers"""
    return x + y

t = (1,2)
#add(t) # it would give us error as the add expects two arguments
add(*t) # it tells take every element from the t, pass it as an argument seperately

"""What if t has more than the required arguemnts"""

v = (1,2,3)
add(*v) # it would also give an error

