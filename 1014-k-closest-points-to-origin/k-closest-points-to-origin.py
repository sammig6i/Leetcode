class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = -(math.sqrt(x**2 + y**2))
            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
                heapq.heappop(heap)
        return [(x, y) for (_, x, y) in heap]
