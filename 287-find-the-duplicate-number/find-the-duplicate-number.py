class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            less_or_equal = sum(1 for n in nums if n <= mid)

            if less_or_equal <= mid:
                low = mid + 1
            else:
                high = mid
        return low