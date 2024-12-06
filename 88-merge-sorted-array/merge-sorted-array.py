class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = len(nums1) - 1
        i = 0

        while n > 0:
            nums1[last] = nums2[i]
            i += 1
            last -= 1
            n -= 1
        
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[j] < nums1[i]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]

        return nums1


        # m = []
        # n = [1]
        
        # m = 1,2,2,3,0,0
        # n = 2,5,6
