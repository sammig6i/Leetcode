class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp = defaultdict(int)
        for start, dest in paths:
            mp[start] += 1
        
        for start, dest in paths:
            if dest not in mp:
                return dest