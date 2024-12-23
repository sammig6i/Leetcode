class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        L = 0
        res = cost = 0

        for R in range(len(s)):
            cost += abs(ord(s[R]) - ord(t[R]))
            if cost > maxCost:
                cost -= abs(ord(s[L]) - ord(t[L]))
                L += 1
            res = max(res, R - L + 1)
        return res