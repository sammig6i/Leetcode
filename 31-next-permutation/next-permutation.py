class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)

        return nums

    def swap(self, nums, L, R):
        nums[L], nums[R] = nums[R], nums[L]

    def reverse(self, nums, start):
        L, R = start, len(nums) - 1
        while L < R:
            self.swap(nums, L, R)
            L += 1
            R -= 1