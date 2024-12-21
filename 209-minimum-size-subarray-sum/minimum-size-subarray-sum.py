class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        res = n + 1
        for i in range(n):
            L, R = i, n
            while L < R:
                m = (R + L) // 2
                curr_sum = prefix[m + 1] - prefix[i]
                if curr_sum >= target:
                    R = m
                else:
                    L = m + 1
            if L < n:
                res = min(res, L - i + 1)
        return res % (n + 1)