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
        """
        adds a point to the array.

        Complexity: Best Case: O(setitem), where setitem is the __setitem__ method in the BinarySearchTree class
                    Worst Case: Same as Best Case
        """
        self.array[item] = item

    def remove_point(self, item: T):
        """
        adds a point to the array.

        Complexity: Best Case: O(delitem), where delitem is the __delitem__ method in the BinarySearchTree class
                    Worst Case: Same as Best Case
        """
        del self.array[item]

    def ratio(self, x: int, y: int) -> list:
        """
        Complexity: Best Case: O(1), when x = 100 or y = 100 or both
                    Worst Case: O((N-(b+d)) * log N), where N is the number of elements in self.array
        """
        res = []

        # Determining the first b elements to exclude
        a = (x/100)*len(self.array)
        b = ceil(a)

        # Determining the last d elements to exclude
        c = (y/100)*len(self.array)
        d = ceil(c)

        # Appending the required elements into the res list
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
