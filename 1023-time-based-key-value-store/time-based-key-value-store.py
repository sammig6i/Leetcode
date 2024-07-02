class TimeMap:

    def __init__(self):
        self.store = {} # k : list of values [valu, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        L, R = 0, len(values) - 1

        while L <= R:
            mid = L + ((R - L) // 2)
            if timestamp < values[L][1]:
                break
            
            res = values[mid][0]

            if values[mid][1] < timestamp:
                L = mid + 1
            elif values[mid][1] > timestamp:
                R = mid - 1
            else:
                return res

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)