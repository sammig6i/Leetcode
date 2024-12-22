class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            min_prefix = min(min_prefix, total)
        
        return -min_prefix + 1
       