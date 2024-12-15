class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                return abs(n)
            nums[idx] *= -1
        # for num in nums :
        #     idx = abs(num) - 1 
        #     if nums[idx] < 0 :
        #         return abs(num)
        #     nums[idx] *= -1
        # return -1