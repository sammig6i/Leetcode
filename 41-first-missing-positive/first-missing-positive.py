class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = [False] * len(nums)
        for n in nums:
            if n > 0 and n <= len(nums):
                seen[n - 1] = True
            
        for n in range(1, len(nums) + 1):
            if not seen[n - 1]:
                return n
        return len(nums) + 1