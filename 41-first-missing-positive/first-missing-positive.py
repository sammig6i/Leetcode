class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # change negative values to zero
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = 0
        
        for n in nums:
            n = abs(n)
            if 1 <= n <= len(nums):
                idx = abs(n) - 1
                if nums[idx] == 0:
                    nums[idx] = -(len(nums) + 1)
                else:
                    nums[idx] = -abs(nums[idx])
        
        for i in range(1, len(nums) + 1):
            idx = i - 1
            if nums[idx] >= 0:
                return i
        return len(nums) + 1


            