from array import array
from random import random

# floats = array('d',(random() for i in range(10**7)))
# print(floats[-1])

# with open('floats.txt','wb') as fp:
#     floats.tofile(fp)

# floats2 = array('d')

# with open('floats.txt', 'rb') as fp:
#     floats2.fromfile(fp,10**7)

# print(floats2[-1])

# print(floats2[-1] == floats[-1])


""" Memory view """
# octets = array('B', (range(10)))

# m1 = memoryview(octets)

# print(m1.tolist())

# print(m1.cast('B', [2,5]).tolist()) # two columns three rows
        # octet = 1,2,3,4,5,6
        # so 
        # 1,2,3
        # 4,5,6

# m2 = m1.cast('B',[5,2])
# print(m2.tolist())

# m2[0,0] = 100
# print(m2.tolist())

# print(octets)

# m2[1,1] = 127
# print(m2.tolist())

numbers = array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv))

print(memv[0])

print(memv.cast('B').tolist())
