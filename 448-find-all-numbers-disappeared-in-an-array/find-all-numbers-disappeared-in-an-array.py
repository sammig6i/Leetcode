class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        res = []
        idx = 0
        for num in range(1, n + 1):
            while idx < n and nums[idx] < num:
                idx += 1
            if idx == n or nums[idx] > num:
                res.append(num)
        return res