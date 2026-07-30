"""namedTuple is a subclass of tuple that returns a class consist of the elements conatined
    in the tuple.

"""

from collections import namedtuple

Location = namedtuple('Location',['latiitude','logitude'])



lahore = Location(12.34,18.90)
print(lahore) # named class has __repr__ implemented

"""namedTuple is subclass of tuple"""
print(issubclass(Location,tuple)) # True




""" shows how we could define a named tuple to hold information about a
city."""
del lahore
City = namedtuple('City','name population district')

lahore = City('Lahore','1.2cr','lhr')
khanqah_dogran = City('Khanqah Dogran','5lac','skp')
print(lahore,khanqah_dogran,sep='  ::  ')
