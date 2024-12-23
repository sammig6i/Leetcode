class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        window_size = 2 * k + 1
        window_sum = 0

        if window_size > n:
            return res
        
        prefix = [nums[0]]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])
        
        for i in range(k, n - k):
            curr_sum = prefix[i + k + 1] - prefix[i - k]
            res[i] = curr_sum // window_size
        return res
# [100000 100000]
