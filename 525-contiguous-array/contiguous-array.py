class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one = 0
        zero = 0
        res = 0

        diff_idx = defaultdict(int)
        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            elif n == 1:
                one += 1
            
            if (one - zero) not in diff_idx:
                diff_idx[one - zero] = i

            if one == zero:
                res = one + zero
            else:
                idx = diff_idx[one - zero]
                res = max(res, i - idx)
            
        return res
            
