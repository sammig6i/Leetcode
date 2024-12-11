class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        # 0,1,3,50,75 low = 0, up = 99

        # -1 lo = -2, upper = -1
        res = []
        if nums[0] > lower:
            res.append([lower, nums[0] - 1])
        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            
            res.append([nums[i] + 1, nums[i + 1] - 1])

            
        
        if upper > nums[len(nums) - 1]:
            res.append([nums[len(nums) - 1] + 1, upper])

        return res