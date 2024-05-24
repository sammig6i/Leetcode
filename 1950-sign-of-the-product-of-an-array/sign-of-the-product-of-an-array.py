class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for n in nums:
            product = n * product
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0

            