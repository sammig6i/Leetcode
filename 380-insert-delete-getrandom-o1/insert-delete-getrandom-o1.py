class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            idx = self.map[val]
            last_val = self.lst[-1]
            self.lst[idx], self.lst[-1] = self.lst[-1], self.lst[idx]
            self.lst.pop()
            self.map[last_val] = idx
            del self.map[val]
            return True
        return False

        # [1, 2, 3, 100]

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()