class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros = ones = res = 0
        diff_idx = defaultdict(int)

        for i, n in enumerate(nums):
            if n == 1:
                ones += 1
            else:
                zeros += 1
            
            if (ones - zeros) not in diff_idx:
                diff_idx[ones - zeros] = i

            if ones == zeros:
                res = ones + zeros
            else:
                idx = diff_idx[ones - zeros]
                res = max(res, i - idx)
        return res
       