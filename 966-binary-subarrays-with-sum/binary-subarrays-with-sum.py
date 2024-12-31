class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cur = 0
        res = 0
        counts = defaultdict(int)
        counts[0] = 1

        for n in nums:
            cur += n
            res += counts[cur - goal]
            counts[cur] += 1
        return res