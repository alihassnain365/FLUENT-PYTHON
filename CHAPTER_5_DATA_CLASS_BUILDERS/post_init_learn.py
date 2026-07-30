"""
In dataclasses, we dont create __init__ manually and it is automatically runs by the dataclass,
so there was a problem, like what if we need to do something before running the __init__ . So thats 
why __post_init__ were introduced.
"""


"""Important!
Please confirm that if the post_init runse before the initialization of the instance attributes 
mean before __init__ or after the __init__ , and one thing to clear also, that the post_init_ run 
before the creation of the instance or object, doesnt the object is created when the __init__ is 
executed.
"""

"""Say, we take (x,y) from user, and x,y should not be negative."""
from dataclasses import dataclass

@dataclass
class Points:
    """Models 2D points, x,y"""
    x : float
    y : float

    def __post_init__(self):
        """checks the positivity of the points"""
        if(self.x < 0 or self.y <0):
            raise TypeError("x,y should be positive")

p1 = Points(1,2)
print(p1)

p2 = Points(-1,2)


