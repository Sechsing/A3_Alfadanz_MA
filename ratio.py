from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree
from referential_array import ArrayR

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.array = []
    
    def add_point(self, item: T):
        self.array.append(item)
    def remove_point(self, item: T):
        self.array.remove(item)

    def ratio(self, x: int, y: int) -> list:
        res = []
        for i in self.array:
            res.append(i)
        a = (x/100)*len(res)
        b = ceil(a)

        c = (y/100)*len(res)
        d = ceil(c)

        for _ in range(b):
            res.remove(min(res))

        for _ in range(d):
            res.remove(max(res))

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
