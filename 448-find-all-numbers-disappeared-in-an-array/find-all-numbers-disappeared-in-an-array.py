class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numSet = set(range(1, n + 1))
        res = []

        for num in nums:
            if num in numSet:
                numSet.remove(num)
            

        return numSet


        