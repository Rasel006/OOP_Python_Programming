""" 
Getter and Setter Methods are used in object-oriented programming languages like Python 
those gives us a controll to get access the private and protected vaulue we can work with them help of  getter and setter method 
 """

""" 
Getter Method : This method is give a ability to read only private and protected value. We can't change vaule whe only getter method is declared 
"""

""" 
Setter Method : This method work with the getter method with this method we can make change in and work with private value outside form the object and subobjects   
"""

class person:
    def __init__(self, Name , age) -> None:
        self.Name = Name
        self.__Age = age
    
    # Getter method 
    @property
    def age(self):
        return self.__Age
    
    # Setter method 
    @age.setter
    def age(self,newage):
        if self.__Age < newage:
            self.__Age = newage

rasel = person("Rasel", 19)
print(rasel.Name,rasel.age) #get value 
# set value 
rasel.age = 20
print(rasel.Name,rasel.age)

        