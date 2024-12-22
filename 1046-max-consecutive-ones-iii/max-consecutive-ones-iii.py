class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = 0
        count = 0
        res = 0
        for R in range(len(nums)):
            if nums[R] == 0:
                count += 1
            
            while count > k:
                if nums[L] == 0:
                    count -= 1
                L += 1
            res = max(res, R - L + 1)
        return res

