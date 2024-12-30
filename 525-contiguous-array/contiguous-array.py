class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_idx = {0: -1}
        diff = 0
        res = 0

        for i, n in enumerate(nums):
            diff += 1 if n == 1 else -1
        
            if diff not in diff_idx:
                diff_idx[diff] = i
            
            if diff == 0:
                res = i - diff_idx[diff]
            else:
                idx = diff_idx[diff]
                res = max(res, i - idx)
        return res