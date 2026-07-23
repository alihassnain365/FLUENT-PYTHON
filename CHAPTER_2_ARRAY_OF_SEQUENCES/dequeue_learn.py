from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)

# now rotating left

 # 0 1 2 3 4 5 6 7 8 9
 # 7 8 9 0 1 2 3 4 5 6

# dq.rotate(3)
# print(dq)

# now rotating right

# 0 1 2 3 4 5 6 7 8 9
# 3 4 5 6 7 8 9 0 1 2

# dq.rotate(-3)
# print(dq)

# adding element at the right at the end of the double ended queue
dq.append(100)
print(dq)

""" As the maximum len of the dequeue is 10
    so if we add a new element after 10, it 
    would wrap around the first one.
"""

# we could also add to the left like add at start
dq.appendleft(12) # so the end element 100 would be removed
print(dq)

dq.extend([100,200,300])
print(dq)

# we could also extend to the start 
dq.extendleft([-1,-2,-3])
print(dq)




