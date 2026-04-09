"""Object Oriented Programming in Python"""
"""it is a programming paradigm that uses objects and classes to structure code. It allows for encapsulation, inheritance, and polymorphism, making it easier to manage and reuse code.
In Python, you can define a class using the `class` keyword. Here's a simple example of a class definition and how to create an object from it:"""


"""Class"""
"""A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. In Python, you can define a class using the `class` keyword. Here's an example of a simple class definition:"""

# class Factory:
#     a = 12 # attribute

#     def hello(self): # method
#         print("Hello, welcome to the factory!")

# print(Factory.a) # Accessing the attribute
# Factory.hello() # Calling the method


"""Object"""
"""An object is an instance of a class. It has its own unique identity and can have different values for the attributes defined in the class. You can create an object from a class by calling the class name as if it were a function. Here's how you can create an object from the `Factory` class:"""

# obj = Factory() # Creating an object
# print(obj.a) # Accessing the attribute through the object
# obj.hello() # Calling the method through the object

"""Constructor"""
"""A constructor is a special method in a class that is automatically called when an object of the class is created. It is used to initialize the attributes of the object. In Python, the constructor is defined using the `__init__` method."""

# class Factory():
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"Your object details are :- Material: {self.material}, Zips: {self.zips}, Pockets: {self.pockets}")

# reebok = Factory("leather", 5, 3)

# campus = Factory("nylon",3,3)

# reebok.show()

# print(reebok.material) # Accessing the attribute of the reebok object



"""Attributes & Methods"""
"""Attributes are variables that belong to an object. They are used to store information about the object. In Python, you can define attributes in the constructor of a class using the `self` keyword. Here's an example of how to define and access attributes in a class:"""
"""Methods are functions that belong to an object. They are used to perform actions on the object or to retrieve information from the object. In Python, you can define methods in a class using the `def` keyword."""
"""Types of Attributes:
1. Instance Attributes: These are attributes that are specific to each instance of a class. They are defined in the constructor using the `self` keyword.
2. Class Attributes: These are attributes that are shared among all instances of a class. They"""


"""Python Decorators in OOPs"""

"""In Python, decorators are a powerful tool that allows you to modify the behavior of functions or methods without changing their actual code. In the context of Object-Oriented Programming (OOP), decorators can be used to enhance or modify the behavior of class methods. 
    There are three main types of decorators in OOP: instance method decorators, class method decorators, and static method decorators."""




# class Animal:
#     name = "lion"  # class attribute

#     def __init__(self, age):
#         self.age = age # instance attribute

#     def show(self): # instance method
#         print(f"How are you? your age is {self.age}")

#     @classmethod
#     def hello(cls): # class method
#         print(f"Hello, I am a {cls.name}")

#     @staticmethod
#     def static():
#         print("how are you?")

# obj = Animal(5)

# obj.show() # Calling the instance method

"""Inheritance in OOPs"""
"""Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes. In Python, you can implement inheritance by defining a new class that takes the parent class as an argument."""

# class Factorymumbai:    # parent class / super class
#     a = "Iam an attribute mentioned inside Factory" # class attribute
#     def hello(self):
#         print("Hello, iam mentioned inside Factory") # method

# class Factorypune(Factorymumbai): # child class / sub class
#     pass

# obj = Factorypune()
# print(obj.a)
# obj.hello()

"""Single Inheritance: In single inheritance, a child class inherits from a single parent class. This is the most common form of inheritance and allows the child class to access the attributes and methods of the parent class."""
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(f"Hello, I am a {self.name}")

# class Human(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         super().show()
#         print(f" I am {self.age} years old.")

# animal1 = Animal("lion")
# person1 = Human("Saurabh",23)

# person1.show()

"""Multiple Inheritance: In multiple inheritance, a child class inherits from multiple parent classes. This allows the child class to access attributes and methods from all the parent classes. However, it can lead to ambiguity if there are conflicting attributes or methods in the parent classes."""

# class Animal:
#     def __init__(self,name):
#         pass

# class Human:
#     def __init__(self,name,age):
#         pass

# class Robot(Animal,Human):
#     name3 = "Saurabh@123"

# obj = Robot("saurabh")


"""Polymorphism in OOPs"""
"""Polymorphism is a concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). In Python, polymorphism can be achieved through method overriding and duck typing."""
"""Method Overriding: This occurs when a child class provides a specific implementation of a method that is already defined in its parent class. The child class's method overrides the parent class's method, allowing for different behavior while maintaining the same interface. example below:"""

# class Animal:
#     def show(self):
#         print("I am a Saurabh")

# class Human(Animal):
#     def show(self):
#         print("I am a Human")

# obj = Human()
# obj.show()

"""Method Overloading: This is a form of polymorphism where multiple methods have the same name but different parameters. However, Python does not support method overloading in the traditional sense, but you can achieve similar functionality using default arguments or variable-length arguments.not supported in python"""

"""Duck Typing: This is a concept in Python where the type or class of an object is less important than the methods it defines. If an object implements a certain method, it can be used in place of any other object that implements the same method, regardless of their class. This allows for greater flexibility and code reuse."""

# class Animal:
#     def show(self):
#         print("I am showing")

# class Human:
#     def show(self):
#         print("hello I am showing")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()

"""Encapsulation in OOPs"""
"""Encapsulation is a fundamental concept in Object-Oriented Programming (OOP) that involves bundling the data (attributes) and methods (functions) that operate on the data within a single unit, typically a class. It also involves restricting direct access to some of an object's components, which is a way of preventing unintended interference and misuse of the data."""
"""In Python, you can achieve encapsulation by using access modifiers. The most common access modifiers are:
1. Public: Attributes and methods that are accessible from anywhere. They are defined without any leading underscores.
2. Protected: Attributes and methods that are intended to be accessed only within the class and its subclasses. They are defined with a single leading underscore (e.g., _attribute).
3. Private: Attributes and methods that are intended to be accessed only within the class. They are defined with a double leading underscore (e.g., __attribute)."""

# class Factory:
#     a = "Pune"

#     def show(self):
#         print("Hello I am a factory")

# obj = Factory()
# print(obj.a) # Accessing the public attribute
# obj.show() # Accessing the public method

# class Factory:
#     a = "Pune" # public attribute
#     _b = "Mumbai" # protected attribute
#     __c = "Delhi" # private attribute


#     def show(self):
#         print("Hello I am a Pune factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super().a) # Accessing the public attribute of the parent class

# obj = Bhopal()
# obj.show2() # Accessing the method of the child class which accesses the attribute of the parent class

# class Factory:
#     __a = "Pune" # private attribute

#     def __show(self):
#         print("Hello I am a Pune factory") # private method

# obj = Factory()
# print(obj.__a) # This will raise an AttributeError because __a is a private attribute
# obj.__show() # This will also raise an AttributeError because __show is a private method


"""Demo"""

# class Demo:
#     def __init__(self):
#         self.name = "Public Member"
#         self._age = 30 # protected member
#         self.__salary = 50000 # private member


#     def show(self):
#         print("Inside the class:")
#         print("Name:", self.name)
#         print("Age:", self._age)
#         print("Salary:", self.__salary)

# obj = Demo()
# obj.show()



"""Abstraction in OOPs"""
"""Abstraction is a fundamental concept in Object-Oriented Programming (OOP) that involves hiding the complex implementation details of an object and showing only the essential features of the object. It allows programmers to focus on what an object does rather than how it does it."""

# from abc import ABC, abstractmethod

# class abstractclass(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     def perimeter(self):
#         pass


# class Square(abstractclass):
#     def __init__(self,side):
#         self.side = side

#     def area(self):
#         print("The area of the square is:", self.side ** 2)

#     def perimeter(self):
#         print("The perimeter of the square is:", 4 * self.side)

# class Circle(abstractclass):
#     def __init__(self,radius):
#         self.radius = radius

#     def perimeter(self):
#         print("The perimeter of the circle is:", 2 * 3.14 * self.radius)

#     def area(self):
#         print("The area of the circle is:", 3.14 * self.radius ** 2)



# obj = Circle(5)
# obj2 = Square(4)

"""Dunder Methods in OOPs"""
"""Dunder methods, also known as magic methods or special methods, are a set of predefined methods in Python that have double underscores (__) at the beginning and end of their names. These methods allow you to define the behavior of your objects in response to built-in operations, such as arithmetic operations, comparisons, and string representations. Dunder methods enable you to customize how your objects interact with various Python features and operators."""


# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return f"This is an animal named {self.name}"
    
# obj = Animal("lion")
# print(obj) # This will call the __str__ method to get the string representation of the object

# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"This is an animal named {self.name}"
    
#     def __add__(self,other):
#         return f"your sum of ages is {self.age + other.age}"
    
# obj = Animal("lion",5)
# obj2 = Animal("tiger",3)

# print(obj + obj2) # This will call the __add__ method to add the ages of the two animals    


# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"This is an animal named {self.name}"
    
#     def __add__(self,other):
#         sum = 0
#         for i in other:
#             sum += i.age
#         return f"your sum of ages is {self.age + sum}"
    
# obj = Animal("lion",5)
# obj2 = Animal("tiger",3)
# obj3 = Animal("elephant",7)

# print(obj + [obj2,obj3]) # This will call the __add__ method to add the ages of the three animals

"""Decorators in OOPs"""
"""Decorators are a powerful feature in Python that allows you to modify the behavior of functions or methods without changing their actual code. In the context of Object-Oriented Programming (OOP), decorators can be used to enhance or modify the behavior of class methods. 
    There are three main types of decorators in OOP: instance method decorators, class method decorators, and static method decorators."""

# class Animal:
#     @property
#     def show(self):
#         print("Hello How are you?")

# obj = Animal()
# obj.show


# def decorate(func):
#     def wrapper():
#         print("I will print myself before the function hello")
#         func()
#         print("I will print myself after the function hello")
#     return wrapper

# @decorate
# def hello():
#     print("Hello How are you?")

# hello()


# def decorate(func):
#     def wrapper(a,b):
#         print("The addition of two numbers is:")
#         func(a,b)
#         print("This is the end of the addition operation.")
#     return wrapper
# @decorate
# def addition(a,b):
#     print(f"The sum of {a} and {b} is: {a + b}")

# addition(5,3)

"""Args and Kwargs in OOPs"""

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)

# addition(1,2,3,4,5)

# def addition(**kwargs):
#     sum = 0
#     for key,value in kwargs.items():
#         sum += value
#     print(sum)

# addition(a=1,b=2,c=3,d=4,e=5)

# def informtion(**kwargs):
#     print("Your information is:")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# informtion(name="Saurabh",age=23,city="Pune",profession="Software Engineer")

# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print("This is the start of the function.")
#         func(*args,**kwargs)
#         print("This is the end of the function.")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(f"The sum of {a} and {b} is: {a + b}")
# addition(5,3)

"""Comprehensions in OOPs"""

# a = 13
# print("even") if a%2 == 0 else print("odd")  # This is a ternary operator, which is a shorthand for an if-else statement. It checks if the number is even or odd and prints the result accordingly.

# l = {i : i**2 for i in range(1,11)} # This is a dictionary comprehension, which is a concise way to create dictionaries. It creates a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers.
# print(l)

"""Lambda Functions in OOPs"""

# Lambda functions are small anonymous functions that can have any number of arguments but can only have one expression.

addition = lambda a,b : a + b # This is a lambda function that takes two arguments and returns their sum.
print(addition(5,3)) # This will call the lambda function to add the two


"""Map, Filter and Reduce in OOPs"""

# a = [1,2,3,4,5]

# result = map(lambda x : x**2,a)

# print(list(result)) # This will print the squares of the numbers in the list a

# a = [1,2,3,4,5]

# def double(x):
#     return x * 2
# result = map(double,a)
# print(list(result)) # This will print the double of the numbers in the list a

# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
    
# a = [1,2,3,4,5]
# result = filter(even,a)
# print(list(result)) # This will print the even numbers in the list a