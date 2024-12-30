class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        res = 0
        curr = 0

        for n in nums:
            curr += n
            res += counts[curr - goal]
            counts[curr] += 1
        return res