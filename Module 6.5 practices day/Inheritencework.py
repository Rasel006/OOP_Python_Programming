""" IN This page we will se about the inheriteenece """
# This the parent Classs or you can say  based Class where form we inherit 
# This call simple inheritence
class animal:
    def __init__(self, Name,Color) -> None:
        self.Name = Name
        self.Color = Color
    
    def Move(self, MoveSpeed):
        self.MoveSpeed = MoveSpeed
    
    def __repr__(self) -> str:
        return f'The Name of the Animal is {self.Name} He\'s / Her Moving speed is {self.MoveSpeed}'

class Lion(animal):
    def __init__(self, Name, Color) -> None:
        super().__init__(Name, Color)
    
    def Move(self, MoveSpeed):
        return super().Move(MoveSpeed)

class Dog(animal):
    def __init__(self, Name, Color) -> None:
        super().__init__(Name, Color)
    
    def Move(self, MoveSpeed):
        return super().Move(MoveSpeed)

class Bird(animal):
    def __init__(self, Name, Color) -> None:
        super().__init__(Name, Color)
    
    def Move(self, MoveSpeed):
        return super().Move(MoveSpeed)

Pegens = Bird('Pegens', 'White')
Pegens.Move('150kmh')

print(Pegens)