class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L, R = 0, len(nums) - 1
        idx = len(nums) - 1
        res = [0] * len(nums)
        while L <= R:
            if abs(nums[L]) > abs(nums[R]):
                res[idx] = nums[L] ** 2
                L += 1
            else:
                res[idx] = nums[R] ** 2
                R -= 1
            idx -= 1
        return res





