class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for n in nums:
            if n:
                prod *= n
            else:
                zero_cnt += 1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, n in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if n else prod
            else:
                res[i] = prod // n
        return res
        
        # prod, zero_cnt = 1, 0
        # for num in nums:
        #     if num:
        #         prod *= num
        #     else:
        #         zero_cnt +=  1
        # if zero_cnt > 1: return [0] * len(nums)

        # res = [0] * len(nums)
        # for i, c in enumerate(nums):
        #     if zero_cnt: res[i] = 0 if c else prod
        #     else: res[i] = prod // c
        # return res