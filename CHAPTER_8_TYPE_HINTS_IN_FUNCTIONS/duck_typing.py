"""In python , if something works like a duck then it is a duck"""

"""for example every objects that has __iterable__ in it they considered
    as the sequnces
"""

"""1. Write a function that counts how many even numbers are present."""
import collections.abc
def even_count(nums: collections.abc.Iterable[int])->int:
    """works for all data types that inherits __iterable__"""
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

# tuple
print(even_count((1,2,3,4,5,6,7,8,9,10)))

# list
print(even_count([1,2,3,4,5,6,7,8,9,10]))

# set 
print(even_count(set((1,2,3,4,5,6,7,8,9,10))))

"""Now write a function that returns the middle element."""

def middle_word(words: collections.abc.Sequence[str])->str:
    """return the middle name """
    return words[len(words)//2]

middle_word(["A", "B", "C"])
# "B"

middle_word(("Ali", "Ahmed", "Sara", "John"))
# "Ahmed"

middle_word("HELLO")
# "L"