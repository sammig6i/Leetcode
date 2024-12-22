class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L = 0
        res = 0
        count = 0
        for R in range(len(nums)):
            if nums[R] == 0:
                count += 1
            
            while count >= 1:
                if nums[L] == 0:
                    count -= 1
                L += 1

            res = max(res, R - L + 1)
        return res