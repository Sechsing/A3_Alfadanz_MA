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
        self.selector = MaxHeap(max_beehives*100)

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.selector = None
        self.selector = MaxHeap(len(hive_list)*100)
        for item in hive_list:
            self.add_beehive(item)

    def add_beehive(self, hive: Beehive):
        honey = hive.nutrient_factor * hive.volume
        harvest = min(hive.capacity, hive.volume) * hive.nutrient_factor
        if honey > 0 and harvest > 0:
            times = int(honey/harvest)
            for i in range(times):
                self.selector.add(harvest)
    
    def harvest_best_beehive(self):
        if len(self.selector) > 0:
            return self.selector.get_max()
