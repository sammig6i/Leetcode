class Solution:

    def __init__(self, w: List[int]):
        self.pre = []
        total = 0
        for weight in w:
            total += weight
            self.pre.append(total)
        
        self.total = total

    def pickIndex(self) -> int:
        L, R = 0, len(self.pre) - 1
        target = random.uniform(0, self.total)
        while L < R:
            m = (R + L) // 2

            if self.pre[m] < target:
                L = m + 1
            elif self.pre[m] > target:
                R = m
            else:
                return L
        return L

# [1,4]
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()