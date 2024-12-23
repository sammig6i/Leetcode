class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        
        
        for i in range(n):
            right = total - nums[i] - left_sum
            
            if right == left_sum:
                return i

            left_sum += nums[i]
        return -1
