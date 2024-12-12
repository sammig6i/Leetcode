class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                heapq.heappush(min_heap, n)
                heapq.heappop(min_heap)
        return min_heap[0]
            