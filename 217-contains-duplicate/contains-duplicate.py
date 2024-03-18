class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        n = 0
        while n < len(nums):
            if nums[n] in hashset:
                return True
            hashset.add(nums[n])
            n += 1
        return False