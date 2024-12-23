class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = max_alt = 0
        n = len(gain)

        prefix = [0] * (n + 1)
        for i in range(len(gain)):
            prefix[i + 1] = prefix[i] + gain[i]
        
        for alt in prefix:
            max_alt = max(max_alt, alt)
        
        return max_alt