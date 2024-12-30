class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        L = 0
        res = 0
        over_k = 0

        for R in range(n):
            freq[nums[R]] += 1

            if freq[nums[R]] == k + 1:
                over_k += 1
            if over_k:
                freq[nums[L]] -= 1
                if freq[nums[L]] == k:
                    over_k -= 1
                L += 1
        return n - L


