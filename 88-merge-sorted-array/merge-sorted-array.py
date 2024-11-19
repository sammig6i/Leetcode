class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_num = len(nums1) - 1
        i = 0

        while n > 0:
            nums1[last_num] = nums2[i]
            i += 1
            last_num -= 1
            n -= 1
        
        nums1.sort()

            
            
        


        