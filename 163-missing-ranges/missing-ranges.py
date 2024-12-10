class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res=[]
        for a in nums + [upper + 1]:
            if a > lower:
                res.append([lower, a - 1])
            lower = a + 1
        return res        



[0, 1, 3, 50, 75]
# 0, 0, 2 [2, 2], [4, 49], [51, 74], [76 - 99]
# nums - sorted unique integers, all elements within range