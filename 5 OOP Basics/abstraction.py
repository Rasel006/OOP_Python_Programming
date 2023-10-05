from abc import ABC, abstractmethod
# abstruct base class

class Bank_vault(ABC):
    def __init__(self, money) -> None:
        self.storage = money

    @abstractmethod #enforce all derived class to have a eat method
    def getMoney(self):
        return self.storage


class Bank(Bank_vault):
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name
        self.__balance = initial_deposit
        super().__init__(initial_deposit)

    def deposit(self, amount):
        self.__balance += amount
        self.storage += amount

    def get_Balance(self):
        return self.__balance

    def getMoney(self):
        return self.storage


towhid_afridi = Bank("Towhid afridi", 50000)
towhid_afridi.deposit(4500)
print(towhid_afridi.getMoney())