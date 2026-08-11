def deco(func):
    print("I am deco")
    def wrapper():
        func()
    return wrapper


@deco
def cutie():
    print("I am cutie pie")


print('Program is starting from here')

