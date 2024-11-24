class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 1 2 -> 3 2 1
        # pivot = 1, 3 2 1

        # 1 3 2 -> 2 1 3
        # pivot = 0, 
        # 1. 2 3 1
        # 2. 

        # 1 1 5 -> 1 5 1
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
            
        if pivot == -1:
            nums.reverse()
            return
        
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        
        
        
        



        
        

        


