class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        for i in range(1, k + len(arr) + 1):
            if i not in arr_set:
                k -= 1
            if k == 0:
                return i


# 2,3,4,7,11 k = 5
# 1,5,6,8,9,10,12,13,14,15

# 1,2,3,4 k = 2
# 5,6,7