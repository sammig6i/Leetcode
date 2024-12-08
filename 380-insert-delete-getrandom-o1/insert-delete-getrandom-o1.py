class RandomizedSet:

    def __init__(self):
        self.list = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.list.append(val)
            self.indices[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indices:
            idx = self.indices[val]
            last_val = self.list[-1]
            self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
            self.list.pop()
            self.indices[last_val] = idx
            del self.indices[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()