class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(n):
            left, right = prefix[i], prefix[-1] - prefix[i] - nums[i]
            if left == right:
                return i
        return -1

[0,1,8,11,17,22,28]

[0,-1,-2,-2,-1,0,0]