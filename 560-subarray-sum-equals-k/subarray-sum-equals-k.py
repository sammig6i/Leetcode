class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums =defaultdict(int)
        prefix_sums[0] = 1
        res = 0
        curr_sum = 0

        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            if diff in prefix_sums:
                res += prefix_sums[diff]
            prefix_sums[curr_sum] += 1
        return res