class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magMap = {}
        for c in magazine:
            magMap[c] = 1 + magMap.get(c, 0)
        
        for c in ransomNote:
            if c in magMap and magMap[c] > 0:
                magMap[c] -= 1
            elif c not in magMap or magMap[c] == 0:
                return False

        return True
