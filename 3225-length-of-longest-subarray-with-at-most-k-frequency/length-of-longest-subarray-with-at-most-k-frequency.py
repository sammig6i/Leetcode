class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        L = 0
        res = 0

        for R in range(len(nums)):
            freq[nums[R]] += 1

            while freq[nums[R]] > k:
                freq[nums[L]] -= 1
                if not freq[nums[L]]:
                    del freq[nums[L]]
                L += 1
            
            res = max(res, R - L + 1)
        return res

[1,2,3,1,2,3,1,2]

