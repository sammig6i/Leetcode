class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for R in range(1, len(nums)):
            if nums[R] == nums[R - 1]:
                return True
        return False

        