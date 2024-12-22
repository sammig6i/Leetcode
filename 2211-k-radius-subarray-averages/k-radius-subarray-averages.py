class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        window_size = 2 * k + 1 

        if window_size > n:
            return res

        prefix = [0] * (n + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        
        
        for i in range(k, n - k):
            left, right = i - k, i + k
            total = prefix[right + 1] - prefix[left]
            res[i] = total // window_size
        return res
            
7,11,14,23,24,32,37,39,45
left = 0
right = 6

