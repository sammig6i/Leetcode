class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s, t):
            mp = {}
            for i in range(len(s)):
                if (s[i] in mp) and mp[s[i]] != t[i]:
                    return False
                mp[s[i]] = t[i]
            return True
        
        return helper(s, t) and helper(t, s)
