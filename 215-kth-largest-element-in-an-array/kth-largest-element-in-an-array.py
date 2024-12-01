class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Helper method to perform the quickselect algorithm
        def quick_select(start, end, k_smallest):
            # If the list contains only one element,
            # return that element
            if start == end:
                return nums[start]
            pivot_index = (start + end) // 2  # Choose the middle element as the pivot
            pivot_value = nums[pivot_index]
            left, right = start - 1, end + 1
          
            # Partition the list such that all elements greater than
            # the pivot are to the left and all elements less than
            # are to the right
            while left < right:
                # Increment left index until finding an element greater than or equal the pivot
                while True:
                    left += 1
                    if nums[left] >= pivot_value:
                        break
                        
                # Decrement right index until finding an element less than or equal the pivot
                while True:
                    right -= 1
                    if nums[right] <= pivot_value:
                        break
                # Swap elements from both sides if needed
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
          
            # If the partitioning index is less than k_smallest, we know that
            # the kth largest element must be in the right partition.
            # If it's greater than or equal to k_smallest, the element will
            # be in the left partition.
            if right < k_smallest:
                return quick_select(right + 1, end, k_smallest)
            return quick_select(start, right, k_smallest)

        # Calculate the 'k_smallest' index based on the 'kth largest' requirement
        n = len(nums)
        k_smallest = n - k
        # Call the quick_select helper function to find the kth largest element
        return quick_select(0, n - 1, k_smallest)

# Note: The variable names 'start', 'end', 'k_smallest', 'pivot_index', 'pivot_value', 'left', and 'right' were chosen to improve clarity and adhere to standard naming conventions.
