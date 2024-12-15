class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        return -1
        
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)
        # return -1