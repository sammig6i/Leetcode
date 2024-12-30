class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_idx = {}
        ones = zeros = res = 0

        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1
            elif n == 1:
                ones += 1
            
            if (ones - zeros) not in diff_idx:
                diff_idx[ones - zeros] = i
            
            if ones == zeros:
                res = ones + zeros
            else:
                idx = diff_idx[ones - zeros]
                res = max(res, i - idx)
        return res