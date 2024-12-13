class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_seen = nums[0]
        L = 1
        for i in range(1, len(nums)):
            if nums[i] != last_seen:
                last_seen = nums[i]
                nums[L] = last_seen
                L += 1
        return L

#  [0,1,1,1,1,2,2,3,3,4]
