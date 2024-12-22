class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = 0
        for R in range(len(nums)):
            k -= 1 - nums[R]
            if k < 0:
                k += 1 - nums[L]
                L += 1

        return R - L + 1
