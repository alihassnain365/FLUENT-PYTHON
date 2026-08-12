"""decorators that doesnt change the argument functions and return the 
    same, but logs it , they are called as decorator register.
"""

registry = []

def regist(func):
    registry.append(func)
    return func

@regist
def login():
    print("login")

@regist
def logout():
    print("Logout")



login()
logout()

print(registry)
