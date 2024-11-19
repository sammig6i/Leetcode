class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.uniform(0, self.total)
        L, R = 0, len(self.prefix_sums) - 1

        while L < R:
            mid = (R + L) // 2

            if self.prefix_sums[mid] < target:
                L = mid + 1
            else:
                R = mid
        return L
        
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()