class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (dist, x, y))
        
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(min_heap)
            res.append([x, y])
        return res

