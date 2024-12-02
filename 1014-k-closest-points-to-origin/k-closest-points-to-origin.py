class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            dist = -math.sqrt((x**2 + y**2))
            if len(res) < k:
                heapq.heappush(res, (dist, x, y))
            else:
                heapq.heappush(res, (dist, x, y))
                heapq.heappop(res)
        return [(x, y) for (_, x, y) in res]

    

    # (-2 - 0) + (2 - 0) = 2.8
    # (1 - 0) + (3 - 0) = 3.16