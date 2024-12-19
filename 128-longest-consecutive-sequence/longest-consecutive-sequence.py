class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for n in nums:
            length = 1
            if (n - 1) not in num_set:
                while (n + length) in num_set:
                    length += 1
            res = max(res, length)
        return res