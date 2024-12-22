class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        L = 0
        max_sum = curr_sum = sum(nums[:k])
        
        for R in range(k, len(nums)):
            curr_sum += nums[R]
            if R - L + 1 > k:
                curr_sum -= nums[L]
                L += 1
            max_sum = max(curr_sum, max_sum)
        return max_sum / k

