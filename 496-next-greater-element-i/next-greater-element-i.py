class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    R = j
                    while R + 1 < len(nums2) and nums2[j] >= nums2[R]:
                        R += 1
                    ans.append(nums2[R] if nums2[R] > nums2[j] else -1)   
        return ans




