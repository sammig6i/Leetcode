class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        L = 0
        
        for R in range(k, len(nums)):
            curr_sum += nums[R]
            curr_sum -= nums[L]
            L += 1
            max_sum = max(max_sum, curr_sum)
        return max_sum / k
