class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = 0, 0
        min_value = float("inf")

        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] == nums2[n2]:
                min_value = min(min_value, nums1[n1])
                n1 += 1
                n2 += 1
            else:
                if nums1[n1] < nums2[n2]:
                    n1 += 1
                else:
                    n2 += 1
        return -1 if min_value == float("inf") else min_value
