class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums


    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i, j in zip(self.nums, vec.nums):
            total += (i*j)
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)