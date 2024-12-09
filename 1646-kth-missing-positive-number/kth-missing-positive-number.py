class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        L, R = 0, len(arr)
        while L < R:
            m = (R + L) // 2

            if (arr[m] - 1) - m < k:
                L = m + 1
            else:
                R = m
        return R + k
        


# 2,3,4,7,11 k = 5
# 1,5,6,8,9,10,12,13,14,15

# 1,2,3,4 k = 2
# 5,6,7