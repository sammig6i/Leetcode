class SparseVector:
    def __init__(self, nums: List[int]):
        # create index-value pairs
        self.hash = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.hash[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        if len(self.hash) < len(vec.hash):
            min_map = self.hash
            other_map = vec.hash
        else:
            min_map = vec.hash
            other_map = self.hash
        for i, n in min_map.items():
            if i in other_map:
                total += (n * other_map[i])
        return total
        
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)