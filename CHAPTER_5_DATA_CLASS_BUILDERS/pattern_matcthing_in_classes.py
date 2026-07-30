"""Question 1 — Employee Database (Keyword Class Patterns)"""

from typing import NamedTuple

class Employee(NamedTuple):
    """Models an Employee"""
    name:   str
    department: str
    salary: int


employees = [
    Employee("Ali", "Engineering", 120000),
    Employee("Sara", "HR", 70000),
    Employee("Ahmed", "Engineering", 95000),
    Employee("Fatima", "Marketing", 85000),
    Employee("Bilal", "Engineering", 150000),
]

"""
Print only the names of employees in Engineering.
Print only the names of employees in HR.
Collect all Engineering salaries into a list.
Print employees earning 120000.
Capture the salary into a variable using a keyword class pattern.
Add a default case that prints "Unknown employee" if nothing matches.
"""

for emp in employees:   
    match emp:
        case Employee(department='Engineering'):
            print(f"Employee's Name is {emp.name}")


# printing the names of the employees in HR

for emp in employees:
    match emp:
        case Employee(department='HR'):
            print(f'Employee name is {emp.name}')

# collect all engineering salaries to a list

eng_employees_salary = list()

for emp in employees:
    match emp:
        case Employee(department='Engineering'):
            eng_employees_salary.append(emp.salary)
print(eng_employees_salary)


# Print employees earning 120000.

for emp in employees:
    match emp:
        case Employee(salary=120000):
            print(f'Employee name {emp.name}')

# Capture the salary into a variable using a keyword class pattern.

for emp in employees:
    match emp:
        case Employee(salary=120000, salary=pay):
            print(f"Employee {emp.name} earns {pay}")
            
