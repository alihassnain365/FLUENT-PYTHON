# def dump(**kwargs):
#     return kwargs

# print(dump(**{'x':1},**{'y':23}))


# d1 = {'a':1,'b':2,'c':3}
# d2 = {'x':10,'y':20,'z':30, 'a':1, 'a':999} # 'a' : 1 would be ignored
# d1 | d2 # this returns the union of the d1 and d2
# print(d1 | d2)

# person = {
#     'name':'Ali Hassnain',
#     'fname': 'ulfat hussain'
# }

# match person:
#     case{
#         'name':'Ali Hassnain', 'fname':"ulfat hussain"
#     }:
#         print('found')

#     case {
#         'name':'ali'
#     }:
#         pass
#     case _:
#         print("default case")
    

b1 = dict(name = 'ali', age = 12, fond = 'cricket')
print(b1)