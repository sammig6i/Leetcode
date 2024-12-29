class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        max_freq = max(num_count.values())
        return sum(freq for freq in num_count.values() if freq == max_freq)