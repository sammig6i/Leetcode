class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
      
        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and n == nums[i - 1]:
                continue
            
            L, R = i + 1, len(nums) - 1

            while L < R:
                three_sum = n + nums[L] + nums[R]
                if three_sum > 0:
                    R -= 1
                elif three_sum < 0:
                    L += 1
                else:
                    res.append([n, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        
        return res

# [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1, 2]