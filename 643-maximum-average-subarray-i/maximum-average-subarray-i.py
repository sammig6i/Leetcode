class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        max_sum = float("-inf")
        L = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            if R - L + 1 == k:
                max_sum = max(curr_sum, max_sum)
                curr_sum -= nums[L]
                L += 1
        return max_sum / k