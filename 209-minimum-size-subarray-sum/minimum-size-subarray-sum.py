class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        res = n + 1
        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l + r) // 2
                curSum = prefix_sum[mid + 1] - prefix_sum[i]
                if curSum >= target:
                    r = mid
                else:
                    l = mid + 1
            if l != n:
                res = min(res, l - i + 1)

        return res % (n + 1)