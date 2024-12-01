class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []
        res = deque([])
        max_height = float("-inf")
    
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                res.appendleft(i)
            max_height = max(max_height, heights[i])
        return list(res)
# 1,3,2,4
# max_view = 4
# res = [3]

# 4,2,3,1
# res = [] 2,3
# max = 3