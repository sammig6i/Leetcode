class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        mp = defaultdict(int)
        L = 0
        res = float("-inf")

        for R in range(len(s)):
            c = s[R]
            mp[c] += 1

            while mp[c] > 1:
                mp[s[L]] -= 1
                if not mp[s[L]]:
                    del mp[s[L]]
                L += 1
            
            res = max(res, R - L + 1)
        
        return res