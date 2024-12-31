class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = {}
        res = 0
        curr = 0
        L = 0

        for i, n in enumerate(nums):
            if n in seen:
                idx = seen[n]
                while L <= idx:
                    curr -= nums[L]
                    L += 1
            seen[n] = i
            curr += n
            res = max(res, curr)
        return res
