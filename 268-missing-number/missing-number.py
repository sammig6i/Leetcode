class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, n in enumerate(nums):
            if n - i > 0:
                return i
        return len(nums)
    
    #  [9,6,4,2,3,5,7,0,1]
