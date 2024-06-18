class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        L = 0
        R = len(height) - 1

        while L < R:
            area = (R - L) * min(height[L], height[R])
            maxArea = max(maxArea, area)

            if height[L] <= height[R]:
                L += 1
            else:
                R -= 1
        return maxArea
