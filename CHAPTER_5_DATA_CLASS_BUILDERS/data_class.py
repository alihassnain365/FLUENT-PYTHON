"""
@dataclass was introduced in Python 3.7 to eliminate the repetitive boilerplate required when 
creating classes whose primary purpose is to store data. By decorating a class with @dataclass, 
Python automatically generates useful methods such as __init__(), __repr__(), and __eq__(), 
allowing you to define a class with only its fields and type hints. Unlike typing.NamedTuple, 
which creates immutable tuple-like objects, dataclasses are mutable by default, meaning their 
attributes can be modified after creation, making them ideal for modeling real-world objects 
whose state changes (e.g., User, Order, Employee, or BankAccount). If immutability is required, 
you can use @dataclass(frozen=True). Dataclasses also support default values, custom methods, and 
full object-oriented behavior, making them the preferred choice in modern Python applications whenever 
you need a lightweight, maintainable class that represents mutable data.
"""



"""
Implement a BankAccount dataclass with the following requirements:

Fields:
owner: str
balance: float = 0
Methods:
deposit(amount)
withdraw(amount) (don't allow overdrafts)
display_balance()

This exercise will help you understand the biggest difference between NamedTuple and dataclass:
NamedTuple is ideal for immutable records, while a dataclass models objects whose state changes 
over time.
"""


from dataclasses import dataclass, field

@dataclass
class BankAccount:
    """Models a Bank system, withdraw , deposit display balance"""
    owner:str
    balance: float = 0

    def deposit(self,amount:int)->None:
        """takes amount and deposit in the account"""
        self.balance += amount

    def withdraw(self, amount:int)->bool:
        """checks amount validity and then do withdraw"""
        if amount > 0 and self.balance > amount:
            self.balance -= amount
            return True
        else:
            return False

    def display(self)->int:
        """returns the balance of the display"""
        return self.balance


ali_hbl = BankAccount('Eleven',1200)
ali_hbl.deposit(400)
ali_hbl.withdraw(399)
print(f"The balanse of {ali_hbl.owner} : {ali_hbl.display()}")



"""
how to manage the class attributes

"""


"""EX - 1.1 The Bug (Don't use default_factory)"""

# @dataclass
# class ShoppingCart:
#     owner: str
#     items : list =[]

# ali_cart = ShoppingCart('ali','laptop')

# shami_cart = ShoppingCart('shami','')

# print(ali_cart.items)
# print(shami_cart.items)

"""this would give us an error becuase all the instances that you would create would share the same
 list with each other. so it would be a buggy list.
 """

@dataclass
class ShoppingCart:
    """Models behaviour of the simple shopping cart"""
    owner: str
    items : list = field(default_factory=list)  # this functin would return a new list for each instance









    