class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, n in enumerate(nums):
            arr.append([n, i])
        
        arr.sort()
        L, R = 0, len(nums) - 1
        while L < R:
            cur = arr[L][0] + arr[R][0]
            if cur == target:
                return [min(arr[L][1], arr[R][1]),
                        max(arr[L][1], arr[R][1])]
            elif cur > target:
                R -= 1
            elif cur < target:
                L += 1
        return []