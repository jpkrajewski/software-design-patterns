from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def __str__(self):
        raise NotImplementedError('You must implement this!')


class Creator(ABC):
    @abstractmethod
    def create(self) -> Product:
        raise NotImplementedError("You should implement this!")


class CarBMW(Product):
    def __str__(self):
        return f'{self.__class__.__name__}'


class BMWFactory(Creator):
    def create(self) -> Product:
        return CarBMW()


class CarLambo(Product):
    def __str__(self):
        return f'{self.__class__.__name__}'


class LamboFactory(Creator):
    def create(self) -> Product:
        return CarLambo()


bmw = BMWFactory().create()
lambo = LamboFactory().create()

print(bmw)
print(lambo)

# CarBMW
# CarLambo




