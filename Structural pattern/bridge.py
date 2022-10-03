from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstraction in bridge pattern"""
    @abstractmethod
    def __init__(self, workshop1, workshop2):
        ...

    @abstractmethod
    def manufacture(self):
        ...


class Plane(Vehicle):
    """Refine abstraction"""
    def __init__(self, workshop1, workshop2):
        self.workshop1 = workshop1
        self.workshop2 = workshop2

    def manufacture(self):
        print(self.__class__.__name__)
        self.workshop1.work()
        self.workshop2.work()
        print('------')


class Boat(Vehicle):
    """Refine abstraction"""
    def __init__(self, workshop1, workshop2):
        self.workshop1 = workshop1
        self.workshop2 = workshop2

    def manufacture(self):
        print(self.__class__.__name__)
        self.workshop1.work()
        self.workshop2.work()
        print('------')


class Workshop(ABC):
    """Implementor"""
    @abstractmethod
    def work(self):
        ...


class Assemble(Workshop):
    """Concrete implementation"""
    def work(self):
        print('Assembled')


class Produce(Workshop):
    """Concrete implementation"""
    def work(self):
        print('Produced')


plane_boeing747 = Plane(Produce(), Assemble())
boat_xxxl = Boat(Produce(), Assemble())

plane_boeing747.manufacture()
boat_xxxl.manufacture()

# Plane
# Produced
# Assembled
# ------
# Boat
# Produced
# Assembled
# ------
