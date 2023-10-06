""" In Here we will see how to overload coampre function made   """

class Person:
    def __init__(self, Name, age, height, weight) -> None:
        self.Name = Name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, Name, age, height, weight) -> None:
        super().__init__(Name, age, height, weight)
    
    # If you want only one campare than use this method 
    def __gt__(self, other):
        return self.age > other.age

# shakib = Cricketer('Sakib', 38, 68, 91)
# musfiq = Cricketer('Rahim', 36, 68, 88)
# kamal = Cricketer('Kamal', 39, 68, 94)
# jack = Cricketer('Jack', 38, 68, 91)
# kalam = Cricketer('Kalam', 37, 68, 95)

# if shakib > musfiq and shakib > kalam and shakib > jack and shakib > kamal:
#     print (f"Name: {shakib.Name} is Older than all.He is {shakib.age} years old")
# elif musfiq > shakib and musfiq > kalam and musfiq > jack and musfiq > kamal:
#         print (f"Name: {musfiq.Name} is Older than all.He is {musfiq.age} years old")
# elif kamal > musfiq and kamal > kalam and kamal > jack and kamal > shakib:
#         print (f"Name: {kamal.Name} is Older than all.He is {kamal.age} years old")
# elif jack > musfiq and jack > kalam and jack > shakib and jack > kamal:
#         print (f"Name: {jack.Name} is Older than all.He is {jack.age} years old")
# elif kalam > musfiq and kalam > shakib and kalam > jack and kalam > kamal:
#         print (f"Name: {kamal.Name} is Older than all.He is {kamal.age} years old")

# if we see the shortCart of those works
cricketers = [
    Cricketer('Sakib', 38, 68, 91),
    Cricketer('Rahim', 36, 68, 88),
    Cricketer('Kamal', 39, 68, 94),
    Cricketer('Jack', 38, 68, 91),
    Cricketer('Kalam', 37, 68, 95)
    ]

older = max(cricketers)
print(older.Name,older.age)