"""lambda is used to create an anonymous function"""

"""we could use lambda to create a reverse list of fruits"""
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits,key=lambda word : word[::-1]))
