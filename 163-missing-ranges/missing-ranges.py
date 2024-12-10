class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not len(nums):
            return [[lower, upper]]
        
        res = []

        if nums[0] > lower:
            res.append([lower, nums[0] - 1])

        for i in range(len(nums)):
            if nums[i] - nums[i - 1] <= 1:
                continue
            
            res.append([nums[i - 1] + 1, nums[i] - 1])

        if nums[len(nums) - 1] < upper:
            res.append([nums[len(nums) - 1] + 1, upper])
        
        return res
            
            
            