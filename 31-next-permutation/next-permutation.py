class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                # nums[i], nums[i + 1] = nums[i + 1], nums[i]
                break

        if pivot == -1:
            nums.sort()
            return nums

        # 132 -> 213
        # 231
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        return nums