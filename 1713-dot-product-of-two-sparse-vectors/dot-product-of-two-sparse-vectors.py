class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i, n in enumerate(nums):
            if n != 0:
                self.pairs.append([i, n])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        i = j = 0

        while i < len(self.pairs) and j < len(vec.pairs):
            if self.pairs[i][0] == vec.pairs[j][0]:
                total += (self.pairs[i][1] * vec.pairs[j][1])
                i += 1
                j += 1
            elif self.pairs[i][0] < vec.pairs[j][0]:
                i += 1
            else:
                j += 1
        return total
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)