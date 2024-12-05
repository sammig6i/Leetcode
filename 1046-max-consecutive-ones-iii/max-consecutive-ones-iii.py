class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        max_ones = 0
        L = 0

        for R, n in enumerate(nums):
            k -= 1 - n
            if k < 0:
                k += 1 - nums[L]
                L += 1
            else:
                max_ones = max(max_ones, R - L + 1)


        
           
        return max_ones
    #                    
    # 1,1,1,0,0,0,1,1,1,1,0 k = 2
    # 1,1,1,0,0,1,1,1,1,1,1
