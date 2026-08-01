"""Create and test a function, then read its __doc__ and check its type"""

def factorial(number:int)->int:
    """returns the factorial of a number"""
    return 1 if number < 2 else number * factorial(number - 1)


# print(factorial(420))
print(factorial.__doc__) # this would return the string literal that we added right after the function definition
        # like this = """returns the factorial of a number"""

print(type(factorial))

""" Use factorial through a different name, and pass factorial as an
argument"""

fact = factorial
print(fact)
print(fact(5))
print(type(fact))

first_11_factorial = list(map(fact,range(11)))
print(first_11_factorial)

