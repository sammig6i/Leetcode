class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        prefix = [nums[0]]
        for n in nums[1:]:
            prefix.append(n + prefix[-1])
        return prefix