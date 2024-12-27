class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_idx = defaultdict(int)
        zero = one = res = 0

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            
            if one - zero not in diff_idx:
                diff_idx[one - zero] = i
            
            if one == zero:
                res = one + zero
            else:
                idx = diff_idx[one - zero]
                res = max(res, i - idx)
        return res




        
            
