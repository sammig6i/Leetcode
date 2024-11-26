class Solution:

    def __init__(self, w: List[int]):
        self.s = []
        total = 0
        for weight in w:
            total += weight
            self.s.append(total)
        self.total = total


    def pickIndex(self) -> int:
        target = random.uniform(0, self.total)
        L, R = 0, len(self.s) - 1

        while L < R:
            m = (L + R) // 2

            if self.s[m] < target:
                L = m + 1
            else:
                R = m
        return L
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()