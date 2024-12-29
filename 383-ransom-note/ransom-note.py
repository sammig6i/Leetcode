class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        mp = defaultdict(int)
        for c in magazine:
            mp[c] += 1
        
        for c in ransomNote:
            if mp[c] <= 0:
                return False
            mp[c] -= 1
        return True
