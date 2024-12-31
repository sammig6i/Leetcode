class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapS, mapT = {}, {}
        for c1, c2 in zip(s, t):
            if c1 in mapS and mapS[c1] != c2:
                return False
            if c2 in mapT and mapT[c2] != c1:
                return False
            mapS[c1] = c2
            mapT[c2] = c1
        return True
