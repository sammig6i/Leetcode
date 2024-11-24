class SparseVector:
    def __init__(self, nums: List[int]):
       self.hash = {i:n for i, n in enumerate(nums) if n != 0}

    
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i, n in self.hash.items():
            if i in vec.hash:
                total += (n * vec.hash[i])
        return total
   

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)