class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix = float("inf")
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            min_prefix = min(min_prefix, total)
        
        start_value = 1
        while start_value + min_prefix < 1:
            start_value += 1
        return start_value

# [-3,2,-3,4,2]
# prefix = [-3, -1, -4, 0, 2]

# [1,-2,-3]
# prefix = [1, -1, -4]

[2,5,10,5,4]