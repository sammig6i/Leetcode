class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = defaultdict(int)
        for c in magazine:
            mp[c] += 1
        
        for c in ransomNote:
            if c not in mp:
                return False
            mp[c] -= 1
            if mp[c] == 0:
                del mp[c]
        return True