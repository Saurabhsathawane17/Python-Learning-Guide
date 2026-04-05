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
class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Hello, I am a {self.name}")

class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        super().show()
        print(f" I am {self.age} years old.")

animal1 = Animal("lion")
person1 = Human("Saurabh",23)

person1.show()

"""Multiple Inheritance: In multiple inheritance, a child class inherits from multiple parent classes. This allows the child class to access attributes and methods from all the parent classes. However, it can lead to ambiguity if there are conflicting attributes or methods in the parent classes."""

class Animal:
    def __init__(self,name):
        pass

class Human:
    def __init__(self,name,age):
        pass

class Robot(Animal,Human):
    name3 = "Saurabh@123"

obj = Robot("saurabh")
