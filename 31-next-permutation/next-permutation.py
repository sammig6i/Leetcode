class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # modify array in place
        # find next larger permuation in lexicographical order
        # if no permutation exists reset the array to the smallest permuation (in ascending order)
        # input = [3 2 1] -> [1 2 3]
        # [3 2 1]
        # input = [1 1 5] -> [1 5 1]
        # [1 5 1]
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                pivot = i
                break
        
        if pivot == -1:
            nums.reverse()
            return nums
        
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        
            
# 3 2 1 -> 1 2 3
# 1 1 5 -> 1 5 1
# 2 3 1 -> 3 1 2
        



