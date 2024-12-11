class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            L = i + 1
            R = len(nums) - 1

            while L < R:
                if (nums[L] + nums[R] + nums[i]) < 0:
                    L += 1
                elif (nums[L] + nums[R] + nums[i]) > 0:
                    R -= 1
                else:
                    res.append([nums[L], nums[R], nums[i]])
                    L += 1
                    R -= 1
                    while L < len(nums) and nums[L] == nums[L - 1]:
                        L += 1
            i += 1
        
        return res

# [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1, 2]