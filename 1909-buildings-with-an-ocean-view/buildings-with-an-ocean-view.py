class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []
        res = deque()
        max_height = float("-inf")

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                res.appendleft(i)
                max_height = heights[i]
        return list(res)