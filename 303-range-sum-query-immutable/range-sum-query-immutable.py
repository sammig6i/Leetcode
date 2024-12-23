class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        self.nums = nums
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        curr_sum = self.prefix[right] - self.prefix[left] + self.nums[right]
        return curr_sum

[0,-2,-2,1,-4,-2,-3]        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)