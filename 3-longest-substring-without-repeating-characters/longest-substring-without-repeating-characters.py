class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        mp = defaultdict(int)
        L = 0
        res = float("-inf")

        for R in range(len(s)):
            c = s[R]
            if c in mp:
                L = max(mp[c], L)
            
            res = max(res, R - L + 1)
            mp[c] = R + 1
        
        return res