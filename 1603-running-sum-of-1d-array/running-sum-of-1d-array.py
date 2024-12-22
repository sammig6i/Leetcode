class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        return prefix