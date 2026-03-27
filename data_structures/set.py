"""Set"""
"""Set is mutable, cannot have duplicates, unordered, Heterogenous"""
# s = {}  # it is dictonary
# print(type(s))

# s = {1,2,3,4,5,5,4}
# print(s)              # it only prints the unique values

"""set don't have any index value and cannot access values through index"""

"""How Set store values in python"""
"""1. Each value in a set is hashed using a hash function (hashed() in Python).
   2. The hash is used as an index to store the element in memory.
   3. since hashing does not maintain order, sets are unordered.
   4. only immutable(hashable) objects can be stored in a set."""


# a = hash("Hello")
# print(a)

# b = hash((1,2,344))
# print(b)

"""Set Traversing"""
"""Set cannot be traversed using index value"""
# a = {1,2,3,4,5}

# for i in a: 
#     print(i)

"""Set Methods"""

a = {1,2,3,4,5}

# a.remove(2)
# print(a)

# a.pop(3)
# print(a)

# a.clear()
# print(a)

# a.discard(5)
# print(a)

# a.add(5)
# print(a)


a = {1,2,3,4,5}
b = {4,5,6,7,8}

# c = a.union(b) 
c = a | b
print(c)

# d = a.intersection(b)
d = a & b
print(d)

# e = a.difference(b)
e = a - b
print(e)

# f = a.symmetric_difference(b)
f = a ^ b
print(f)