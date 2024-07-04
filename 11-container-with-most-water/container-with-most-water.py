class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxArea = 0

        while L < R:
            area = min(height[L], height[R]) * (R - L)
            maxArea = max(area, maxArea)
            if height[L] <= height[R]:
                L += 1
            else:
                R -= 1
        return maxArea