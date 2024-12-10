class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        missing_ranges = []

        if n == 0:
            return [[lower, upper]]

        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])

        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue

            missing_ranges.append([nums[i] + 1, nums[i + 1] - 1])

        if upper > nums[n - 1]:
            missing_ranges.append([nums[n - 1] + 1, upper])

        return missing_ranges  

[0, 1, 3, 50, 75], 100
# 0, 0, 2 [2, 2], [4, 49], [51, 74], [76 - 99]
# nums - sorted unique integers, all elements within range