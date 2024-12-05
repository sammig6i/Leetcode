class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = 0
        max_cons = 0
        for R, n in enumerate(nums):
            k -= 1 - n
            if k < 0:
                k += 1 - nums[L]
                L += 1
            else:
                max_cons = max(max_cons, R - L + 1)
        return max_cons
