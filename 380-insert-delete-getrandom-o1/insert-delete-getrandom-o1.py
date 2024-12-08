from random import random

class RandomizedSet:

    def __init__(self):
        self.list = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        self.list.append(val)
        self.indices[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        idx = self.indices[val]
        last_val = self.list[-1]
        self.indices[last_val] = idx
        self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
        
        self.list.pop()
        del self.indices[val]
        return True


    def getRandom(self) -> int:
        return self.list[int(random() * len(self.list))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()