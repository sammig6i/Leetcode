class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        window, countT = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        res, resLen = [-1, -1], float('inf')
        have, need = 0, len(countT)

        L = 0
        for R in range(len(s)):
            c = s[R]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = (R - L + 1)
                c = s[L]
                window[c] -= 1
                if c in countT and window[c] < countT[c]:
                    have -= 1
                L += 1
        L, R = res
        return s[L: R + 1] if resLen != float('inf') else ""

