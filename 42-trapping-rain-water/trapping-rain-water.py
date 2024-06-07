class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        maxL = height[L]
        maxR = height[R]
        waterCount = 0

        while L < R:

            if maxL <= maxR:
                L += 1
                maxL = max(height[L], maxL)
                waterCount += maxL - height[L]
            else:
                R -= 1
                maxR = max(height[R], maxR)
                waterCount += maxR - height[R]
        return waterCount 
            