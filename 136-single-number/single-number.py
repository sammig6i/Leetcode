class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for n in nums:
            res ^= n
        return res