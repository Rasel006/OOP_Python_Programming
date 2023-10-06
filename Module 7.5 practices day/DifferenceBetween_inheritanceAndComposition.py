""" 
Composition vs Inheritance  
 It’s big confusing among most of the people that both the concepts are pointing to Code Reusability then what is the difference b/w Inheritance and Composition and when to use Inheritance and when to use Composition? 

Inheritance is used where a class wants to derive the nature of parent class and then modify or extend the functionality of it. Inheritance will extend the functionality with extra features allows overriding of methods, but in the case of Composition, we can only use that class we can not modify or extend the functionality of it. It will not provide extra features. Thus, when one needs to use the class as it without any modification, the composition is recommended and when one needs to change the behavior of the method in another class, then inheritance is recommended.

 """

# example of Inheritance: 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name)  # Output: "Buddy"
print(dog.speak())  # Output: "Woof!"
print(cat.name)  # Output: "Whiskers"
print(cat.speak())  # Output: "Meow!"

# example of conpositol 
class engin: 
    def __init__(self) -> None:
        pass

    def Soundofeneng(self, sound):
        print("The sound is",sound)

class bmw:
    def __init__(self,Name) -> None:
        self.Name = Name

    def soundOfEngin(self,sound):
        self.endgin = engin()
        self.sound = engin().Soundofeneng(sound)

CarBmw = bmw("BMW V8")

CarBmw.soundOfEngin("Rataataatatata")