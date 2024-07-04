class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        L = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            length = R - L + 1
            if length - max(count.values()) <= k:
                res = max(res, length)
            else:
                count[s[L]] = count.get(s[L], 0) - 1
                L += 1
        return res
                

       