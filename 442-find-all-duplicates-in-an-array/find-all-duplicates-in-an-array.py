class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            n = abs(n)
            idx = n - 1
            if nums[idx] < 0:
                res.append(n)
            nums[idx] = -abs(nums[idx])

        return res
        
[-4,3,2,-7,8,2,-3,-1]

[-1,-1,2]