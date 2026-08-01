"""Factorial implemented with reduce and an anonymous function"""
from functools import reduce
def factorial(number:int) ->int:
    """retunrs the factorial of a number"""
    return reduce(lambda a,b: a*b, range(1,number+1))

print(factorial(8))



