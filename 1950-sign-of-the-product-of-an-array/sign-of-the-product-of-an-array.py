class Solution:
    def arraySign(self, nums: List[int]) -> int:
        flag = True

        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                flag = not flag
        return 1 if flag else -1
            