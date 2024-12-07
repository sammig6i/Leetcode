class SparseVector:
    def __init__(self, nums: List[int]):
        self.map = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.map[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i, n in vec.map.items():
            if i in self.map:
                total += (self.map[i] * n)
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)