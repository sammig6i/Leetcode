class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        def quickSelect(start, end, k_smallest):
            if start == end:
                return nums[start]
            pivot = (start + end) // 2

            pivot_val = nums[pivot]
            L, R = start - 1, end + 1

            while L < R:
                while True:
                    L += 1
                    if nums[L] >= pivot_val:
                        break
                
                while True:
                    R -= 1
                    if nums[R] <= pivot_val:
                        break
                
                if L < R:
                    nums[L], nums[R] = nums[R], nums[L]
            
            if R < k_smallest:
                return quickSelect(R + 1, end, k_smallest)
            return quickSelect(start, R, k_smallest)

        n = len(nums)
        k_smallest = n - k

        return quickSelect(0, n - 1, k_smallest)
        

