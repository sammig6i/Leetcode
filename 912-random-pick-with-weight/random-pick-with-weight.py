class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.pre = []
        for weight in w:
            self.total += weight
            self.pre.append(self.total)
                

    def pickIndex(self) -> int:
        L, R = 0, len(self.pre) - 1
        target = random.uniform(0, self.total)

        while L < R:
            m = (R + L) // 2
            if self.pre[m] >= target:
                R = m
            else:
                L = m + 1
        return L
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()