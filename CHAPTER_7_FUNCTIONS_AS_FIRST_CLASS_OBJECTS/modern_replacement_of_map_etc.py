"""we could use genexps as a modern replacement to the functions"""

def facotrial(n:int)->int:
    """returns the facotorial of a number"""
    return 1  if n < 2 else n * facotrial (n - 1)

first_11 = list(map(facotrial,range(0,11)))
print(first_11)

"""now we could skip the map, """
del first_11

first_11 = [facotrial(n) for n in range(11)]
print(first_11)

