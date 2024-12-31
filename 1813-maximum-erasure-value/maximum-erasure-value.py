class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        L = 0
        res = 0
        curr = 0

        for R in range(len(nums)):
            curr += nums[R]
            counts[nums[R]] += 1

            while counts[nums[R]] > 1:
                curr -= nums[L]
                counts[nums[L]] -= 1
                L += 1
            
            res = max(res, curr)
        return res
