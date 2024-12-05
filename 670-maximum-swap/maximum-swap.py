class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        max_val = "0"
        max_i = -1
        swap_i = swap_j = -1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > max_val:
                max_val = nums[i]
                max_i = i
            if nums[i] < max_val:
                swap_i = max_i
                swap_j = i
        nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]
        return int("".join(nums))
