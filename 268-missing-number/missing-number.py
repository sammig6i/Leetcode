class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for i, v in enumerate(nums):
            if v - i > 0:
                return i
        return n

        