from abc import ABC, abstractmethod
from tkinter import N

class GameAI(ABC):
    """Template method defines the skeleton of an algorithm in a method"""
    def turn(self) -> None:
        self.move()
        self.gather_resources()
        self.build()
        self.choose_target()
        self.attack()
        self.special_move()

    @abstractmethod
    def move(self) -> None:
        ...

    def gather_resources(self) -> None:
        print('Gathering closest resources...')

    @abstractmethod
    def build(self) -> None:
        ...
    
    @abstractmethod
    def choose_target(self) -> None:
        ...

    def attack(self) -> None:
        print(f'Dealt {self.damage} damage to {self.target}.')

    @abstractmethod
    def special_move(self) -> None:
        ...


class MonsterAI(GameAI):
    damage = 10
    target = None

    def move(self) -> None:
        print('Moving towards the closest hero by 1 unit...')

    def build(self) -> None:
        """Monsters don't build"""
        pass

    def choose_target(self) -> None:
        self.target = 'Hero'
        print('Choosing the closest hero...')

    def special_move(self) -> None:
        """Monsters don't have special moves"""
        pass

class GhostAI(GameAI):
    damage = 15
    target = None

    def move(self) -> None:
        print('Moving towards the closest hero by 2 units even if there is a obstacle')

    def build(self) -> None:
        """Ghosts don't build"""
        pass

    def choose_target(self) -> None:
        self.target = 'Random Hero'
        print('Chosing random hero...')

    def special_move(self) -> None:
        print('Dissapearing...')


monster = MonsterAI()
monster.turn()
# Moving towards the closest hero by 1 unit...
# Gathering closest resources...
# Choosing the closest hero...
# Dealt 10 damage to Hero.

ghost = GhostAI()
ghost.turn()
# Moving towards the closest hero by 2 units even if there is a obstacle
# Gathering closest resources...
# Chosing random hero...
# Dealt 15 damage to Random Hero.
# Dissapearing...
     