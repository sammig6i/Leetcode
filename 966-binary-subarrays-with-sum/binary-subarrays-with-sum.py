class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        res = 0
        cur = 0

        for n in nums:
            cur += n
            res += counts[cur - goal]
            counts[cur] += 1
        return res

