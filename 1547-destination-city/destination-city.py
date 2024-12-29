class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp = {}
        for start, dest in paths:
            mp[start] = dest
        
        for start, dest in paths:
            if dest not in mp:
                return dest