class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones = zeros = 0
        res = 0
        diff_idx = {}

        for i, n in enumerate(nums):
            if n == 1:
                ones += 1
            else:
                zeros += 1
            
            diff = ones - zeros
            if diff not in diff_idx:
                diff_idx[diff] = i
            
            if ones == zeros:
                res = ones + zeros
            else:
                idx = diff_idx[diff]
                res = max(res, i - idx)
        return res