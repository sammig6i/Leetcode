class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_idx = {}
        ones = zeros = 0
        res = 0

        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1
            else:
                ones += 1
            
            diff = ones - zeros
            if diff not in diff_idx:
                diff_idx[diff] = i
            
            if diff == 0:
                res = ones + zeros
            else:
                idx = diff_idx[diff]
                res = max(res, i - idx)
        return res