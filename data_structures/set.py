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

a = {1,2,3,4,5}

for i in a:
    print(i)
