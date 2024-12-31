class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapST, mapTS = {}, {}
        for i in range(len(s)):
            if s[i] in mapST and mapST[s[i]] != t[i]:
                return False
            if t[i] in mapTS and mapTS[t[i]] != s[i]:
                return False
            mapST[s[i]] = t[i]
            mapTS[t[i]] = s[i]
        return True
