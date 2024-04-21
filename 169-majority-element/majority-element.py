class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}
        size = len(nums)
        for n in nums:
            if n in countMap:
                countMap[n] += 1
            else:
                countMap[n] = 1
        
        for num, count in countMap.items():
            if count > (size // 2):
                return num
        