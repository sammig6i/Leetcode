class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                max_idx, max_val = i + 1, nums[i + 1]
                break
        else:
            return num
        
        for j in range(i + 1, len(nums)):
            if max_val <= nums[j]:
                max_idx, max_val = j, nums[j]
        
        left_idx = i
        for j in range(i, -1, -1):
            if nums[j] < max_val:
                left_idx = j
        
        nums[left_idx], nums[max_idx] = nums[max_idx], nums[left_idx]
        return int("".join(nums))


    # 988368