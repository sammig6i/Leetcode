class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(n):
            left = prefix[i]
            right = prefix[-1] - prefix[i + 1]
            if left == right:
                return i
        return -1
