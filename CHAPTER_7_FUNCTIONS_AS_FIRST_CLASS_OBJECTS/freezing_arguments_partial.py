"""Using partial to use a two-argument function where a one-argument
callable is required"""

from operator import mul
from functools import partial

# print(mul(4,5))  = 20

numbers = [i for i in range(1,11)]

"""suppose we want to multiply 3, with entire list"""

"""There are two options."""
# 1.
for i in range(len(numbers)):
    numbers[i] = mul(numbers[i],3)

# 2 .

numbers = [i for i in range(1,11)]

mul_by_3 = partial(mul,3)
"""this becomes a function, that multiply the given argument by 3"""

# print(mul_by_3(7))  = 21
print(list(map(mul_by_3,numbers)))

"""the main job of the partial is two freeze the arguments, like they must already be in the function
    argument list."""
# mul_by_3(8,9) = TypeError








