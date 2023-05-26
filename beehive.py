from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        """
            Constructs the BeehiveSelector class
            :complexity best: O(max_beehives) where the method constructs a heap of max_beehives size
            :complexity worst: O(max_beehives) same as best case
        """
        self.selector = MaxHeap(max_beehives*100)

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
            Replaces the current beehives in the selector with input
            :complexity best: O(M+M*add_beehive) where M is the number of elements in hive_list and add_beehive is the
             complexity of the add_beehive method when the method recreates the selector using len(hive_list) as the
             input and performs the add_beehive method for M times
            :complexity worst: O(M+M*add_beehive) same as best case
        """
        self.selector = None
        self.selector = MaxHeap(len(hive_list)*100)
        for item in hive_list:
            self.add_beehive(item)

    def add_beehive(self, hive: Beehive):
        """
            Adds the beehive into the selector while sorting the selector
            :complexity best: O(logN) where N is the number of elements in the heap when harvest is bigger than honey
            and the method only adds harvest into selector once, the add operation for heap is of log N complexity
            :complexity worst: O(mlogN) where m is the number of times harvest can be deducted from honey when the
            method adds harvest into selector m times and the add operation costs logN complexity
        """
        honey = hive.nutrient_factor * hive.volume
        harvest = min(hive.capacity, hive.volume) * hive.nutrient_factor
        while harvest < honey:
            self.selector.add(harvest)
            honey -= harvest
        harvest = honey
        self.selector.add(harvest)
    
    def harvest_best_beehive(self):
        """
            Returns the beehive that is most profitable with get_max method in MaxHeap
            :complexity best: O(1) where the get_max method returns the first element from the array if selector is not
            empty
            :complexity worst: O(1) same as best case
        """
        if len(self.selector) > 0:
            return self.selector.get_max()
