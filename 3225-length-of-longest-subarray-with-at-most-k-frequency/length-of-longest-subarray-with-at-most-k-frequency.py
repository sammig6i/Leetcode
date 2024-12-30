class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        L = -1
        res = 0

        for R in range(len(nums)):
            freq[nums[R]] += 1

            while freq[nums[R]] > k:
                L += 1
                freq[nums[L]] -= 1
            
            res = max(res, R - L)
        return res


