class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = max(freq for n, freq in Counter(nums).items())

        res = 0
        for n, freq in Counter(nums).items():
            if freq == max_freq:
                res += freq
        return res