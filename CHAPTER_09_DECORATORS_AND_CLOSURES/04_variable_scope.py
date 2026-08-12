"""If a name is assigned anywhere inside a function, 
Python treats that name as local throughout that function,
 unless you explicitly declare it global or nonlocal."""

a = 100

def func(b):
    print(b)
    print(a)
    a = 10
# UnboundLocalError: cannot access local variable
#  'a' where it is not associated with a value

func(11)
    