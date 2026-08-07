"""if we want a tuple to store any numbers of any same data type"""

def take_int(user:tuple[int, ...])->None:
    """prints the tuple of int"""
    print(user)

take_int((10,20,30,40)) # we dont need to write tuple[int,int,int,int]


"""Now if we want take any tuple of any type like str,int, float or mixed"""
from typing import Any
def take_any_type(user:tuple[Any, ...]) -> None:
    """prints the tuple with any data type"""
    print(user)

take_any_type((10,'ali',90.7))
# mypy would not give us an error