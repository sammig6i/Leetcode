class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        prefix = []
        for n in nums:
            total += n
            prefix.append(total)
        return prefix