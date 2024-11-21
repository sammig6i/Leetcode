class SparseVector:
    def __init__(self, nums: List[int]):
        # nums1 = 1 0 0 2 3 nums2 = 0 3 0 4 0
        # 1*0 + 0*3 + 0*0 + 2*4 + 3*0
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i, j in zip(self.nums, vec.nums):
            total += (i*j)
        return total
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)