class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        L, R = 0, len(arr)

        while L < R:
            m = (R + L) // 2
            if (arr[m] - m) - 1 < k:
                L = m + 1
            else:
                R = m
        return R + k

