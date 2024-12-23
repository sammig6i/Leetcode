class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i, v in enumerate(nums):
            if v - i > 0:
                return i
        return n