class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        for i, h in enumerate(heights):
            while res and heights[res[-1]] <= h:
                res.pop()
            res.append(i)
        return res


# 4,2,3,1
# [0,2]