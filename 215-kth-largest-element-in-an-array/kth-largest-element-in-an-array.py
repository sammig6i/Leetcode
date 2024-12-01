class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                if n > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, n)
        return heap[0]

        # 3,2,3,1,2,4,5,5,6 k=5
        # 3,4,5,5,6
            
