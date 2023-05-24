from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    d1: BeeNode | None = None
    d2: BeeNode | None = None
    d3: BeeNode | None = None
    d4: BeeNode | None = None
    d5: BeeNode | None = None
    d6: BeeNode | None = None
    d7: BeeNode | None = None
    d8: BeeNode | None = None
    subtree_size: int = 1

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        if point[0] < self.key[0] and point[1] < self.key[1] and point[2] >= self.key[2]:
            if self.d1 is None or self.d1.key == point:
                return self
            return self.d1.get_child_for_key(point)
        elif point[0] < self.key[0] and point[1] >= self.key[1] and point[2] < self.key[2]:
            if self.d2 is None or self.d2.key == point:
                return self
            return self.d2.get_child_for_key(point)
        elif point[0] >= self.key[0] and point[1] < self.key[1] and point[2] < self.key[2]:
            if self.d3 is None or self.d3.key == point:
                return self
            return self.d3.get_child_for_key(point)
        elif point[0] < self.key[0] and point[1] >= self.key[1] and point[2] >= self.key[2]:
            if self.d4 is None or self.d4.key == point:
                return self
            return self.d4.get_child_for_key(point)
        elif point[0] >= self.key[0] and point[1] >= self.key[1] and point[2] < self.key[2]:
            if self.d5 is None or self.d5.key == point:
                return self
            return self.d5.get_child_for_key(point)
        elif point[0] >= self.key[0] and point[1] < self.key[1] and point[2] >= self.key[2]:
            if self.d6 is None or self.d6.key == point:
                return self
            return self.d6.get_child_for_key(point)
        elif point[0] > self.key[0] and point[1] > self.key[1] and point[2] > self.key[2]:
            if self.d7 is None or self.d7.key == point:
                return self
            return self.d7.get_child_for_key(point)
        else:
            if self.d8 is None or self.d8.key == point:
                return self
            return self.d8.get_child_for_key(point)

    def set_subtree_size(self, subtree_size: int) -> None:
        self.subtree_size = subtree_size

class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """
        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode:
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        elif key[0] < current.key[0] and key[1] < current.key[1] and key[2] >= current.key[2]:
            return self.get_tree_node_by_key_aux(current.d1, key)
        elif key[0] < current.key[0] and key[1] >= current.key[1] and key[2] < current.key[2]:
            return self.get_tree_node_by_key_aux(current.d2, key)
        elif key[0] >= current.key[0] and key[1] < current.key[1] and key[2] < current.key[2]:
            return self.get_tree_node_by_key_aux(current.d3, key)
        elif key[0] < current.key[0] and key[1] >= current.key[1] and key[2] >= current.key[2]:
            return self.get_tree_node_by_key_aux(current.d4, key)
        elif key[0] >= current.key[0] and key[1] >= current.key[1] and key[2] < current.key[2]:
            return self.get_tree_node_by_key_aux(current.d5, key)
        elif key[0] >= current.key[0] and key[1] < current.key[1] and key[2] >= current.key[2]:
            return self.get_tree_node_by_key_aux(current.d6, key)
        elif key[0] > current.key[0] and key[1] > current.key[1] and key[2] > current.key[2]:
            return self.get_tree_node_by_key_aux(current.d7, key)
        else:
            return self.get_tree_node_by_key_aux(current.d8, key)

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)
        self.root.set_subtree_size(self.length)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        if current is None:
            current = BeeNode(key, item=item)
            self.length += 1
        elif key != current.key:
            if key[0] < current.key[0] and key[1] < current.key[1] and key[2] >= current.key[2]:
                current.d1 = self.insert_aux(current.d1, key, item)
            elif key[0] < current.key[0] and key[1] >= current.key[1] and key[2] < current.key[2]:
                current.d2 = self.insert_aux(current.d2, key, item)
            elif key[0] >= current.key[0] and key[1] < current.key[1] and key[2] < current.key[2]:
                current.d3 = self.insert_aux(current.d3, key, item)
            elif key[0] < current.key[0] and key[1] >= current.key[1] and key[2] >= current.key[2]:
                current.d4 = self.insert_aux(current.d4, key, item)
            elif key[0] >= current.key[0] and key[1] >= current.key[1] and key[2] < current.key[2]:
                current.d5 = self.insert_aux(current.d5, key, item)
            elif key[0] >= current.key[0] and key[1] < current.key[1] and key[2] >= current.key[2]:
                current.d6 = self.insert_aux(current.d6, key, item)
            elif key[0] > current.key[0] and key[1] > current.key[1] and key[2] > current.key[2]:
                current.d7 = self.insert_aux(current.d7, key, item)
            else:
                current.d8 = self.insert_aux(current.d8, key, item)
            current.set_subtree_size(current.subtree_size+1)
        else:
            raise ValueError('Inserting duplicate item')
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        return current.d1 is None and current.d2 is None and current.d3 is None and current.d4 is None and current.d5 is None and current.d6 is None and current.d7 is None and current.d8 is None

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
