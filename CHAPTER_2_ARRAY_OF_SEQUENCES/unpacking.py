
# a,b,c,*rest = range(10)
# print(a,b,c,rest)

# a,b,*rest = range(5)
# print(a,b,rest)


"""*args can appear in any position"""

# *rest,a,b = range(10)
# print(rest,a,b)


# *rest,a,b = range(1) # this would give not enough value 
#                     # to unpack error
# print(rest,a,b)

# a,b,*rest,c,d = range(10)
# print(a,b,rest,c,d)


# def fun(a,b,c,d,*rest):
#     print(a,b,c,d,rest)

# fun(*[1,2],3,*[1,2,3,4,5])

""" could also use the unpacking while difining list , tuples"""

# list_unpack = [*range(10),*['ali','shehri','shami']]
# print(list_unpack)

# tuple_unpack = (*range(8),*('ali','shehri','shami'))
# print(tuple_unpack)


"""pattern matching with match/case like switch case in c++"""

# def who_is_this(code_name):
#     match code_name:
#         case 'a':
#             print('this is ali')
#         case 's':
#             print('this is shehri')
#         case 't':
#             print('this is sunny')
#         case 'i':
#             print('this is shami')
#         case _:
#             raise ProcessLookupError('No match case')

# who_is_this('z')


