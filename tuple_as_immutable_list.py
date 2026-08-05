"""if we want a tuple to store any numbers of any same data type"""

def take_int(user:tuple[int, ...]):
    """prints the tuple of int"""
    print(user)

take_int((10,20,30,40)) # we dont need to write tuple[int,int,int,int]
