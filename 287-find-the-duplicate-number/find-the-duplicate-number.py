class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for b in range(32):
            x = y = 0
            mask = 1 << b

            for num in nums:
                if num & mask:
                    x += 1
            
            for num in range(1, n):
                if num & mask:
                    y += 1
            
            if x > y:
                res |= mask
        return res