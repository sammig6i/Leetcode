class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # [3,2,1,5,6,4]
        # 1,2,3,4,5,6
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            k -= 1
            if k == 0:
                return nums[i]
