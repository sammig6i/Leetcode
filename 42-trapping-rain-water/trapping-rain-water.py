class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        res = 0
        maxL = height[L]
        maxR = height[R]

        while L < R:
            if maxL < maxR:
                L += 1
                maxL = max(height[L], maxL)
                res += maxL - height[L]
            else:
                R -= 1
                maxR = max(height[R], maxR)
                res += maxR - height[R]
        return res
                


