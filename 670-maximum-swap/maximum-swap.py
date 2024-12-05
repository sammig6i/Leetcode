class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                max_val = nums[i + 1]
                max_i = i + 1
                break
        else:
            return num

        for j in range(i + 1, len(nums)):
            if max_val <= nums[j]:
                max_i = j
                max_val = nums[j]
        
        left_i = j
        for j in range(i, -1, -1):
            if nums[j] < max_val:
                left_i = j
        nums[max_i], nums[left_i] = nums[left_i], nums[max_i]
        return int("".join(nums))
