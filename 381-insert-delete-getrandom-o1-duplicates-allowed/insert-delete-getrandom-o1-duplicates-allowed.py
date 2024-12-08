class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        self.list.append(val)
        if val in self.indices:
            self.indices[val].add(len(self.list) - 1)
            return False
        
        self.indices[val] = {len(self.list) - 1}
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        idx = self.indices[val].pop()
        last_val = self.list[-1]
        self.list[idx], self.list[-1] = self.list[-1], self.list[idx]

        self.indices[last_val].add(idx)
        self.indices[last_val].remove(len(self.list) - 1)
        self.list.pop()

        if not self.indices[val]:
            del self.indices[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()