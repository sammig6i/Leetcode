class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            n = abs(n)
            idx = n - 1
            nums[idx] = -(abs(nums[idx]))
        
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res
        
    [-4,-3,-2,-7,8,2,-3,-1]
        
    