"""Exercise 1 — Your First Decorator"""
# def deco(func):
#     def wrapper():
#         print("Function is about to run.")
#         func()
#         print("Function is run is finished")
#     return wrapper

# @deco
# def greet():
#     print("Hello, Ali")



# greet()


"""Exercise 2 — Decorators With Function Arguments"""

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments({args})")
        result = func(*args,**kwargs)
        print(f"Result = {result}")
    return wrapper

@logger
def add(a,b):
    return a+b

@logger
def multiply(a,b):
    return a*b

add(2,3)
multiply(5,4)





