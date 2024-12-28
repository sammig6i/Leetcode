class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        diff_idx = {0: -1}
        diff = 0

        for i, n in enumerate(nums):
            diff += 1 if n == 1 else -1
            
            if diff in diff_idx:
               res = max(res, i - diff_idx[diff])
            else:
                diff_idx[diff] = i
            
        return res
            
