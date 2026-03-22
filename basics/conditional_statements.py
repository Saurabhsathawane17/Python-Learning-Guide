"""Conditional Statements"""
# if, if-else, if-elif-else - this are the types 
# Que. Accept two numbers and print the greatest between them.

# a = int(input('Enter a :'))
# b = int(input('Enter b :'))
# if a > b:
#     print(f'{a} is greater than {b}')
# else:
#     print(f'{b} is greater than {a}')


# Que. Accept the gender from the user as char and print the respective greeting message

# Gender = input("Enter your gender(M or F):")

# if Gender =='M' or Gender == 'm':
#     print(f'Good Morning Sir')
# elif Gender == 'F' or Gender == 'f':
#     print(f'Good Morning Mam')
# else:
#     print("Undefined Gender")

# Que. Accept an integer and check whether it is an even number or odd
# a = int(input("Enter a number:"))

# if a%2 == 0:
#     print(f"{a} is an even number")
# else:
#     print(f"{a} is an odd number")


# Que. Accept name and age from the user. check if the user is a valid voter or not.

# name = input("Enter your name:")
# age = int(input("Enter your age:"))

# if age >=18:
#     print(f"{name} you are eligible to vote")
# else:
#     print(f"{name} you are not eligible to vote")

# Que. Accept a year and check if it is a leap year or not

# year = int(input("Enter a year:"))

# if year%4 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# if year%100 == 0 and year%400 == 0:
#     print("Its a leap year")
# elif year%100 != 0 and year%4 == 0:
#     print("Its a leap year")
# else:
#     print("Its a normal year")

"""if-elif ladder"""

# temp = float(input("Enter a temperature:"))

# if temp < 0:
#     print("Its a Freezing Cold")

# elif temp >= 0 and temp < 10:
#     print("Its a Very Cold")

# elif temp >= 10 and temp < 20:
#     print("Its a Cold")

# elif temp >= 20 and temp < 30:
#     print("Its a Pleasant")

# elif temp >= 30 and temp < 40:
#     print("Its a Hot")

# else:
#     print("Its a Very Hot")