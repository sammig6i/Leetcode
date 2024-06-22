class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        leftMax = 0
        rightMax = 0
        waterCount = 0

        while L < R:
            leftMax = max(leftMax, height[L])
            rightMax = max(rightMax, height[R])

            if rightMax < leftMax:
                R -= 1
                maxR = max(0, rightMax - height[R])
                waterCount += maxR
            else:
                L += 1
                maxL = max(0, leftMax - height[L])
                waterCount += maxL
        return waterCount
        