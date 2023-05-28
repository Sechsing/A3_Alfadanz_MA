from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree
from referential_array import ArrayR

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.array = BinarySearchTree()

    def add_point(self, item: T):
        self.array[item] = item
    def remove_point(self, item: T):
        del self.array[item]

    def ratio(self, x: int, y: int) -> list:
        res = []

        a = (x/100)*len(self.array)
        b = ceil(a)

        c = (y/100)*len(self.array)
        d = ceil(c)

        for key in range(len(self.array)):
            if (key > b) and (key <= (len(self.array)-d)):
                element = self.array.kth_smallest(key, self.array.root)
                res.append(element.key)

        return res


if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    print(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
