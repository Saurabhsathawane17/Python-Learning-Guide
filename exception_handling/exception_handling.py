"""Errors"""
"""Errors occurs due to mistakes in the code that prevent it from running.
    these can syntax errors or logical errors or indentation errors or type errors"""


"""Exceptions"""
"""Exceptions are unexpected events or errors that occur during the execution of a program."""

"""Try and Except"""

# a = int(input("Enter a number:"))

# try:
#     print(10/a)

# except ZeroDivisionError:
#     print("You cannot divide by zero")

# print("Ok I have done the division")


"""err"""

# a = int(input("Enter a number:"))

# try:
#     print(10/a)

# except Exception as e:
#     print(f"sorry there is an error {e}")

# print("Ok I have done the division")

"""else"""

# a = int(input("Enter a number:"))

# try:
#     print(10/a)

# except Exception as e:
#     print(f"sorry there is an error {e}")

# else:
#     print("Good there is no error")

# print("Ok I have done the division")

"""finally"""

# a = int(input("Enter a number:"))

# try:
#     print(10/a)

# except Exception as e:
#     print(f"sorry there is an error {e}")

# else:
#     print("Good there is no error")

# finally:
#     print(f"I will run no matter what {a}")

# print("Ok I have done the division")

"""raise"""

age = int(input("Enter a Age:"))

try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("You are eligible")

except Exception as e:
    print(f"An error occured {e}")

print("The club will be start soon..!! stay tuned...")