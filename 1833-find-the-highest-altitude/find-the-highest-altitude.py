class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = max_alt = 0
        n = len(gain)

        prefix = [0] * (n + 1)
        for i in range(len(gain)):
            total += prefix[i] + gain[i]
            max_alt = max(max_alt, total)
        return max_alt