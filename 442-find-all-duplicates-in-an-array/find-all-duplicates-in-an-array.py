class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            n = abs(n)
            idx = n - 1
            if nums[idx] < 0:
                res.append(n)
            nums[idx] = -nums[idx]
        return res