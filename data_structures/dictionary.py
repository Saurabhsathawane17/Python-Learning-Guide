"""Dictionary in python"""
"""It is mutable,Keys must be unique but values can be duplicates, it follows the insertion order, Heterogenous"""

# d = {1:"hello",2:"world",3:"python"}

# print(d)

a = {1:100,2:200,3:300,4:400,5:500}

# print(a[1])
# a[1] = 1000   # update value of key 1 or updating
# print(a[1])

# a[6] = 600  # creating   
# print(a)
# del a[6]    # deleting

# print(a)

# for i in a:
#     print(i)       # only keys
#     print(a[i])    # only values
#     print(i,a[i])  # both keys and values

# help(dict)

"""Dictionary questions"""

# Que. 1 write a python script to merge two Python dictionaries.

# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)


# Que. 2 write a python program to sum all the values in a dictionary.

# d1 = {10:100,20:200,30:300}

# sum = 0
# for i in d1:
#     sum = sum + d1[i]

# print(sum)

# Que. 3 write a python program to multiply all the values in a dictionary.

# Que. 4 count the frequency of each elements

# a = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,6,7,8]

# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d)


# Que. 5 write a python program to combine two dictionary by adding values for common keys.

d1 = {10:100,20:200,40:400}
d2 = {40:400,50:500,60:600}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)