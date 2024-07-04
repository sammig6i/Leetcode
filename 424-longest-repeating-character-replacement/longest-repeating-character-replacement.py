class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0 
        maxLength = 0
        maxF = 0
        count = {}

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxF = max(count[s[R]], maxF)
            while (R - L + 1) - maxF > k:
                count[s[L]] -= 1
                L += 1
            maxLength = max(maxLength, R - L + 1)
        return maxLength