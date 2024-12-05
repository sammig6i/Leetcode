class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            dist = -(math.sqrt(x**2 + y**2))
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, x, y))
            else:
                if dist > max_heap[0][0]:
                    heapq.heappush(max_heap, (dist, x, y))
                    heapq.heappop(max_heap)

        return [[x, y] for _, x, y in max_heap]

