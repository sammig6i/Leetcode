class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        diff_idx = [None] * (2 * n + 1)
        count = 0
        res = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count == 0:
                res = i + 1
            
            if diff_idx[count + n] is not None:
                res = max(res, i - diff_idx[count + n])
            else:
                diff_idx[count + n] = i
        return res
