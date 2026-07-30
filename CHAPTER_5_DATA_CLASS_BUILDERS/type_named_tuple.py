"""
typing.NamedTuple was introduced to solve a limitation of collections.namedtuple:
while collections.namedtuple creates lightweight, immutable tuple-like objects with 
named fields, it doesn't provide built-in type annotations, making it harder for IDEs 
and static type checkers (like mypy) to understand the expected types of each field. 
typing.NamedTuple uses a class-based syntax with type hints 
(e.g., class User(NamedTuple): name: str; age: int), making code more readable, 
easier to maintain, and better supported by modern development tools, while still 
behaving like an immutable tuple. Both are useful for representing simple records 
such as coordinates, database rows, configuration values, or API responses, but in 
modern Python, typing.NamedTuple is generally preferred because it combines the 
efficiency of tuples with the benefits of static typing.
"""

"""Exercise 1 — Store API/User Data (Beginner)
    ("Ali", "ali@gmail.com", 21)
    Requirements
Create User with fields:
name
email
age
Create an object.
Print every field using dot notation.
Verify that indexing still works.
"""

from typing import NamedTuple

class User(NamedTuple):
    """Models the response from the API as a USER instance"""
    name:str
    email:str
    age:int


ali = User("Ali", "ali@gmail.com", 21) 
# print(ali.name)
# print(ali.email)
# print(ali.age)



"""Exercise 2 — Employee Records (Intermediate)
    [
    ("Ali", 45000),
    ("Sara", 70000),
    ("Ahmed", 55000),
    ("Zain", 30000)
    ]

Requirements
Create an Employee namedtuple.
Convert every tuple into an Employee.
Print only employees earning more than 50000.
"""

class Employee(NamedTuple):
    """Models the Employee"""
    name:str
    salary:int

hr_records = [
    ("Ali", 45000),
    ("Sara", 70000),
    ("Ahmed", 55000),
    ("Zain", 30000)
    ]

# now creating the instance of each record

employees = [Employee(name,salary) for name,salary in hr_records]

"""employee is a list that containse the instances of the class Employee"""

required_employees = [emp for emp in employees if emp.salary > 50000]
print(required_employees)



"""Exercise 3 — Processing API Responses"""

weather_api_response = [
    ("Lahore", 36.5, 58),
    ("Karachi", 33.2, 72),
    ("Islamabad", 29.8, 65),
    ("Murree", 18.4, 80)
]

class WeatherReport(NamedTuple):
    """Models the weather api response as weather report"""
    city_name: str
    temperature: float
    humidity: int

"""now creating a list that containse the instances of each city and its data"""

cities_weather_report = [WeatherReport(city_name,temperature,humidity) for city_name,temperature,humidity in weather_api_response]

"""Now printing """

for city in cities_weather_report:
    print(f"{city.city_name} : {city.temperature} , {city.humidity} %")

