class Vector2D:
    """Models the behaviour of the 2D vectors"""
    
    def __init__(self,x,y):
        """Initializes the X and Y axis"""
        self.x = x
        self.y = y

    def __repr__(self):
        """Represents the instance"""
        return f"Vector2D(x={self.x!r},y={self.y!r})"
    
    def __add__(self, other):
        """adds two vectors"""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __bool__(self):
        """Implements the bool behaviour of the instance"""
        return (self.x or self.y)

v1 = Vector2D(1,2)
v2 = Vector2D(3,4)
print(v1 + v2)
print(v1)


        