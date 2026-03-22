"""Loops in Python"""
"""There are two types of loops in python
1. for loop
2. while loop"""

# for loop
# range() function - (start,end,steps)

# a = range(1,21,1)

# for i in a:
#     print(i)

# for i in range(1,21,1):
#     print(i)

# for i in range(21):
#     print(i)

# for i in range(20,51):
#     print(i)


# for i in range(16,0,-1):
#     print(i)

# for i in range(-5,-16,-1):
#     print(i)

# for i in range(5,51,5):
#     print(i)

# Print a table of 5
# n = int(input("Which table you want to print:"))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

"""Loops for strings"""
# a = "Artificial Intelligence"

# print(len(a))

# for i in range(len(a)):    
#     print(a[i])

# for i in a:
#     print(i)

# for char in a:     
#     print(char)

# for i in range(23):
#     print(i)

# for i in range(1,21):
#     if i == 15:
#         continue
#     print(i)


"""Break and Continue statement"""
# for i in range(1,21):
#     if i == 15:
#         print("Break statement is executed")
#         break
#     print(i)

# else:
#     print("Else statement is executed")


"""For Loop Questions"""
# Que.1 Accept an integer and print hello world n times

# n = int(input("Enter a number:"))

# for i in range(n):
#     print("Hello World")

# Que.2 Print natural number up to n
# n = int(input("Enter a number:"))
# for i in range(1,n+1):
#     print(i)

# Que.3 Reverse for loop. print n to 1
# n = int(input("Enter a number:"))
# for i in range(n,0,-1):
#     print(i)

# Que.4 Take a number as input and print its table
# n = int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# Que.5 Sum up to n terms.
# n = int(input("Enter a number:"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

# Que.6 Factorial of a number
# n = int(input("Enter a number:"))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

# Alternative: to find factors 
# n = int(input("Enter a number:"))
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)


#*** Que.7 Print sum of all even and odd numbers in a range
# n = int(input("Enter a number:"))
# sum_even = 0
# sum_odd = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         even = sum_even + i
#     else:
#         odd = sum_odd + i

# print(f"Your even sum is {even}")
# print(f"Your odd sum is {odd}")

# Que.8 Accept a number and check if it is a perfect number or not?.
# A number whose sum of factors is equal to the number itself ex: 6 = 1,2,3 = 6

# n = int(input("Enter a number:"))

# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum = sum + i

# if sum == n:
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number")

# Que.9 Check whether the number is prime or not?
# n = int(input("Enter a number:"))

# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count = count + 1

# if count == 2:
#     print(f"{n} is a prime numbers")
# else:
#     print(f"{n} is not a prime numbers")

# Que.10 Reverse a string without using in build functions.

# a = "Saurabh"
# print(a[::-1])
# b = ""
# for i in range(len(a) - 1, -1, -1):
#     b = b + a[i]
# print(b)

# Que. 11. Check string is palindrome or not
# a = "Saurabh"
# b = ""
# for i in range(len(a) -1, -1, -1):
#     b = b + a[i]

# if b == a:
#     print(f"{a} is a palindrome")
# else:
#     print(f"{a} is not a palindrome")

""" Que. 12. Count all letters, digits and special symbols from a given string
Given: str1 = "P@#yn26at^&i5ve"
Expected Outcome:
Total counts of chars, digits and symbols 
Chars = 8 
Digits = 3 
Symbol = 4"""


# a = "P@#yn26at^&i5ve"
# dig = 0
# char = 0
# spchar = 0
# for i in a:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         spchar += 1

# print(f"your digits are {dig}")
# print(f"your characters are {char}")
# print(f"your special characters are {spchar}")

# print(dir(str))

"""While loop"""

# a = 1
# while a <= 10:
#     print(a)
#     a += 1

"""While loop questions"""
# Que. 1 Separate each digits of a number and print it on the new line.

# a = int(input("Enter a number:"))

# while a > 0:
#     digit = a % 10
#     print(digit)
#     a = a // 10

# Que. 2 Accept a number and print its reverse

# a = int(input("Enter a number:"))

# rev = 0

# while a > 0:
#     digit = a % 10
#     rev = rev * 10 + digit
#     a = a // 10

# print(rev)

# Que. 3 Accept a number and check if it is a palindromic number (if number and its reverse are equal)

# a = int(input("Enter a number:"))

# copy = a
# rev = 0 
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10


# if copy == rev:
#     print("Its a palindromic number")
# else:
#     print("Its not a palindromic number")

"""Create a random number gussing game"""