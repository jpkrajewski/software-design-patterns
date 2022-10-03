import abc
from typing import List, Type
from random import shuffle


class SortingStrategy(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def sort_list(array: List[int]) -> List[int]:
        ...


class AscendingSortStrategy(SortingStrategy):

    @staticmethod
    def sort_list(array: List[int]) -> List[int]:
        return sorted(array.copy())


class DescendingSortStrategy(SortingStrategy):

    @staticmethod
    def sort_list(array: List[int]) -> List[int]:
        return sorted(array.copy(), reverse=True)


class RandomSortStrategy(SortingStrategy):

    @staticmethod
    def sort_list(array: List[int]) -> List[int]:
        array = array.copy()
        shuffle(array)
        return array


class Sorter:
    def __init__(self, array: List[int], sorting_strategy: Type[SortingStrategy]):
        self.array = array
        self.sorting_strategy = sorting_strategy

    def sort(self) -> None:
        if not issubclass(self.sorting_strategy, SortingStrategy):
            raise TypeError(f'Sorting strategy must inherit from {SortingStrategy.__name__} '
                            f'not {self.sorting_strategy.__name__}')
        print(self.sorting_strategy.sort_list(self.array))


array = [1, 5, 6, 3, 5, 6]

sorter_asc = Sorter(array=array, sorting_strategy=AscendingSortStrategy)
sorter_asc.sort()
# [1, 3, 5, 5, 6, 6]

sorter_desc = Sorter(array=array, sorting_strategy=DescendingSortStrategy)
sorter_desc.sort()
# [6, 6, 5, 5, 3, 1]

sorter_random = Sorter(array=array, sorting_strategy=RandomSortStrategy)
sorter_random.sort()
# shuffled array

bad_sorter = Sorter(array=array, sorting_strategy=dict)
bad_sorter.sort()
# TypeError: Sorting strategy must inherit from SortingStrategy not dict