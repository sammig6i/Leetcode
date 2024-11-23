class Solution:

    def __init__(self, w: List[int]):
        self.s = []
        total = 0
        for weight in w:
            total += weight
            self.s.append(total)
        self.total = total

    def pickIndex(self) -> int:
        L, R = 0, len(self.s) - 1
        target = random.uniform(0, self.total)
        while L < R:
            m = (L + R) // 2

            if self.s[m] >= target:
                R = m
            else:
                L = m + 1
        return L




        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()