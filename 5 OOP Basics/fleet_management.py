class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.buses = []
        self.routes = []
        self.counters = []
        self.managers = []
        self.supervisors = []
        self.fare = []


class Driver:
    def __init__(self, name, license, age):
        self.name = name
        self.age = age
        self.license = license


class Counter:
    def __init__(self):
        pass

    def purchase_a_ticket(self, start, destination):
        pass


class Passenger:
    def __init__(self):
        pass


class Supervisor:
    def __init__(self):
        pass