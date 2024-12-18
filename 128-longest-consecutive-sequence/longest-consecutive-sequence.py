class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        res = 0

        for n in nums:
            if not d[n]:
                d[n] = d[n - 1] + d[n + 1] + 1
                d[n - d[n - 1]] = d[n]
                d[n + d[n + 1]] = d[n]
                res = max(res, d[n])
        return res