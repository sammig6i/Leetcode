class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        window_size = 2 * k + 1
        n = len(nums)
        res = [-1] * n
        if window_size > n:
            return res
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(k, n - k):
            left_bound, right_bound = i - k, i + k
            curr_sum = prefix[right_bound + 1] - prefix[left_bound]
            avg = curr_sum // window_size
            res[i] = avg
        return res