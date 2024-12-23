class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        res = [-1] * n


        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        
        for i in range(k, n - k):
            res[i] = (pre[i + k + 1] - pre[i - k]) // window_size
        return res

    