class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_idx = {}
        count = 0
        res = 0

        for i, n in enumerate(nums):
            count += 1 if n == 1 else -1
            
            if count not in diff_idx:
                diff_idx[count] = i
            
            if count == 0:
                res = i + 1
            else:
                idx = diff_idx[count]
                res = max(res, i - idx)
        return res