class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[nums[i]] = i