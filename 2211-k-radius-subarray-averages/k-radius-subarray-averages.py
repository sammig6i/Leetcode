class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        window_sum = 0
        res = [-1] * n

        if window_size > n:
            return res
        
        for i in range(n):
            window_sum += nums[i]

            if i - window_size >= 0:
                window_sum -= nums[i - window_size]

            if i >= window_size - 1:
                res[i - k] = window_sum // window_size
        return res