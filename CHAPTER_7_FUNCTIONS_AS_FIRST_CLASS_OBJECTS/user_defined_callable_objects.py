""" A BingoCage does one thing: picks items from a shuffled list"""
import random
class BingoCage:
    """pick a shuffled random from the given list"""

    def __init__(self,items):
        """creates an instance of items"""
        self._items = items
        random.shuffle(self._items)

    def pick(self):
        """picks an item from shuffled list"""
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty BingoCage')

    def __call__(self):
        return self.pick()

bg1 = BingoCage([1,2,3,4,5,6,7,8])
print(bg1()) # would return a random number from the list

        


    