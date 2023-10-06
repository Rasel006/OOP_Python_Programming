"""
 Class Method:
Class method is a decorator function built that is an expression that evaluate when it define.
And it is a function inside a class that can be called on the class itself.We define is with @classmethod.It must have an perameter Called cls.Class methods are often used for tasks like creating instances of the class or performing operations that affect the class as a whole.
 """

""" 
Static Method :
A static method in Python is like a regular function but is defined inside a class. It doesn't depend on the class or its instances and doesn't have access to class-level or instance-specific data.We define it with @staticmethod decorator function. They are often used for functions that are logically connected to a class but don't require access to its attributes or methods.

 """

""" Difference Between  Class method and Static method with example """

# NO: 1. Access to Class and Instance Attributes
""" 
Class Methods: Class methods have access and have access to modifiy the attribute under the class level. It also have perameter instance access but that cant modified

Static method : Static methods have no access to instance-specific attributes or methods and are primarily used for utility functions that are not tied to the class or its instances.
 """
#  Example :
class myClass: 
    class_arrtribute = 10
     
    def __init__(self, instacnce_atrribute) -> None:
        self.instacnce_atrribute = instacnce_atrribute
    
    @classmethod
    def classMethod(self):
        self.class_arrtribute += 2
    
    @staticmethod
    def staticMethod():
        print("This is static method")

# NO: 2. Method Invocation:
""" 
Class Method: Class methods can be called on both the class itself and its instances. They receive the class as their first parameter, usually named cls.

Static Method: Static methods can be called on both the class and its instances, but they do not receive any special first parameter.
 """
# Example:
myClass.classMethod()  # Calling class method on the class
obj = myClass(20)
obj.classMethod()  # Calling class method on an instance
obj.staticMethod()  # Calling static method on an instance
""" 
3. Inheritance Behavior:

Class Method: Class methods can be overridden by subclasses, and the overridden method in the subclass will be called if invoked through the subclass.

Static Method: Static methods cannot be overridden in subclasses. They behave the same way in both the base class and its subclasses. """
# Example:
class BaseClass:
    @classmethod
    def method(cls):
        print("BaseClass method")

class SubClass(BaseClass):
    @classmethod
    def method(cls):
        print("SubClass method")

# Calling the overridden method in the subclass
obj = SubClass()
obj.method()  # Output: "SubClass method"

# Calling the base class method
base_obj = BaseClass()
base_obj.method()  # Output: "BaseClass method"

""" 
4. Use Case:

Class Method: Class methods are often used for factory methods, methods that create instances of the class, and for methods that need to access or modify class-level attributes or methods.

Static Method: Static methods are used for utility functions or methods that do not depend on class or instance attributes, such as conversion functions or helper functions that are related to the class but don't need access to its state.

Example:
 """
class TemperatureConverter:
    @classmethod
    def celsius_to_fahrenheit(cls, celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084

# Using class method to convert temperature
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(25)

# Using static method to convert meters to feet
feet = TemperatureConverter.meters_to_feet(2)
""" 
These differences highlight when and how to use class methods and static methods in Python classes based on their intended use cases and access to class and instance attributes. """