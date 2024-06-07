class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        maxL = 0
        maxR = 0
        waterCount = 0

        while L < R:
            maxL = max(height[L], maxL)
            maxR = max(height[R], maxR)

            if maxL <= maxR:
                L += 1
                diff = maxL - height[L]
                waterCount += max(diff, 0)
            else:
                R -= 1
                diff = maxR - height[R]
                waterCount += max(diff, 0)
        return waterCount 
            