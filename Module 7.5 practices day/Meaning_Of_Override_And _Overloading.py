"""
    Oparator Over Loading

Oparator over Loading is a Fearturs of OOP(Object Oriented Programming). That gives you extar Power ,flexibility etc. By use Oparator overloading we can use oparator in custom or user define data type . If We Look at " + " oparator we will see that in can sum two numbers concat to string , merge list because of this define with int and str class but it can't not merge two objects . It will give error because compile don't how comibine two object.For this we define a method to do the work this call oparator Over loading.We can oveer Load all the oparator but we can't create new Oparator.For doing over loading python give us spacial function the autometicly invoks the opartor works.

How it works:
 If we talk about + oparator in python you can overload + oparator by make __add__ function on the class and in function we can make our own way to do the work.

Let's see an Example: 
"""


class OparatorOverloading:
    def __init__(self, name) -> None:
        self.Name = name

    def __add__(self, other):  # This how over Loading works we need give a perameter for recevied the another object that going to be merge
        return self.Name + other.Name


print(1 + 1)  # this normal + how it woks
a = OparatorOverloading("Rasel")
b = OparatorOverloading("Rean")

print(a + b)  # when i don't create over laoding method in the it gives error

"""  
    Method Overrideing :

Method Overriding means that Whe we hava Parent Class(super class) and Child Class(derived) and there method are same name , same signature  but we need to customize the method that called Method overriding. This a fearture of OOP(Object Oriented Programming).We can call method overiding as runtime polymorphism. Where method overriding always required inheritence.For method overiding we need at least two class.

Let's see and example :
"""


class animal:
    def __init__(self, name) -> None:
        self.Name = name

    def sound(self, sound):
        self.sound = sound


class dog(animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def sound(self, Dog_sound):
        return f"This overrinden method value is {Dog_sound}"


class cat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def sound(self, Catsound):
        return f"This overrindend method value is {Catsound}"


dogSound = dog("Scobby")
print(dogSound.sound("bow bow"))
catSound = cat("smith")
print(catSound.sound("meowh meowh"))