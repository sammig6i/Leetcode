class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        L = 0
        res = 0
        cost = 0
        n = len(s)
        
        for R in range(len(s)):
            cost += abs(ord(s[R]) - ord(t[R]))

            while cost > maxCost:
                cost -= abs(ord(s[L]) - ord(t[L]))
                L += 1
            
            res = max(res, R - L + 1)
        return res

