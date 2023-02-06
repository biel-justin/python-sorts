from abc import ABC, abstractmethod


class Sorter(ABC):
    @abstractmethod
    def sort(self):
        pass

    def less(self, v: int, w: int) -> bool:
        return v < w

    def swap(self, a: list, i: int, j: int) -> None:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
