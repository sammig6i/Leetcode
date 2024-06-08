class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftMax = 0
        rightMax = 0
        l, r = 0, len(height) - 1

        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])

            if rightMax < leftMax:
                res += rightMax - height[r]
                r -= 1
            else:
                res += leftMax - height[l]
                l += 1
        return res
            
        
