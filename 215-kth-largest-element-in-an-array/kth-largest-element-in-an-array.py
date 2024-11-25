class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # [3,2,1,5,6,4]
        return heapq.nlargest(k, nums)[-1]
        
        

        

