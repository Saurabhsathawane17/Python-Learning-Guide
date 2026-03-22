"""Data Structures in Python"""
"""List"""
"""It allows Mutability, duplicates, ordered, Heterogenous"""

# a = [11,12,13,14,15,16,17,70.33,print()]
# b = [32,9,1,34,20,13,20,30,21]

# 1st way using index
# for i in range(len(a)):
#     print(a[i])

# 2nd way directly on values
# for i in a:
#     print(i)

"""Methods in List"""
# # 1. append()
# a.append(18)   # append 18 to the end
# print(a)

# # 2. insert()
# a.insert(2,8) # insert 8 at index 2
# print(a)

# # 3. extend()
# a.extend([20,21,22])   # extend the list by adding multiple elements at the end
# print(a)

# # 4. remove()
# a.remove(11)    # remove the first occurrences of 11
# print(a)

# 5. pop()
# popped_item = a.pop(8)   # removes and store the element at index 3
# print(popped_item)
# print(a)

# 6. index()
# index = a.index(13)       # finds the index of 13
# print(index)

# 7. count()
# count_17 = a.count(17)      # count occurences of 17
# print(count_17)

# 8. sort()
# b.sort()     # sorts the list in ascending order
# print(b)

# 9. reverse()
# b.reverse()   # reverses the list
# print(b)

# 10. clear()
# b.clear()    # removes all elements from the list
# print(b)


"""Questions on list"""

# Que. 1 Print positive and negative elements of list

# l = [-3,-5,2,4,8,9,-1]

# positive_list = []
# negative_list = []

# for i in l:
#     if i >= 0:
#         positive_list.append(i)
#     else:
#         negative_list.append(i)

# print(positive_list)
# print(negative_list)


# Que. 2 Mean of list element

# l = [10,15,20,25,30,35,40]
# sum = 0
# for i in l:
#     sum = sum + i

# mean = sum / len(l)
# print(mean)

# Que 3 Find the greatest elements and print its index too

# l = [10,15,20,25,30,35,40]

# max = l[0]
# for i in l:
#     if i > max:
#         max = i

# print(i)

# Alternative solution:

# l = [12,50, 43, 256, 347, 45, 8]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"The largest element is {largest} and its index is {index}")

# Que 4 Find the second greatest element.

# l = [10,15,20,25,30,35,40]

# max = l[0]
# second_max = l[0]
# for i in l:
#     if i > max:
#         second_max = max
#         max = i

# print(second_max)

# Alternative solution:

# largest = l[0]
# second_largest = l[0]

# for i in l:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i != largest:
#         second_largest = i

# print(second_largest)

# Que 5 Check if the list is sorted or not.

# l = [10,15,20,25,30,35,40]

# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("List is not sorted")
#         break
# else:
#     print("List is sorted")

# Alternative solution:

# l = [10,15,20,25,30,35,40]

# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("List is not sorted")
#         break
# else:
#     print("List is sorted")