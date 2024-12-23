class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_set = set(nums)

        for i in range(0, n):
            if i not in num_set:
                return i
        return n