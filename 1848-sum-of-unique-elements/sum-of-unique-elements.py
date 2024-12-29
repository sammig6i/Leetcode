class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        return sum(n for n in num_count if num_count[n] == 1)