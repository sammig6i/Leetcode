class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        def quickSelect(start, end, k_smallest):
            if start == end:
                return nums[start]
            pivot = (start + end) // 2

            pivot_val = nums[pivot]
            L, R = start, end

            while True:
                while L <= end and nums[L] < pivot_val:
                    L += 1
                while R >= start and nums[R] > pivot_val:
                    R -= 1
                if L >= R:
                    break  # Pointers have crossed, partitioning is done
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R -= 1
            
            if R < k_smallest:
                return quickSelect(R + 1, end, k_smallest)
            return quickSelect(start, R, k_smallest)

        n = len(nums)
        k_smallest = n - k

        return quickSelect(0, n - 1, k_smallest)
        

