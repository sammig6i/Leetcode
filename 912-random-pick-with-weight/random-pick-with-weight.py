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
            mid = (R + L) // 2

            if self.s[mid] >= target:
                R = mid
            else:
                L = mid + 1

        return L

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()