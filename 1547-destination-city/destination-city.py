class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp = {p[0]: p[1] for p in paths}

        start = paths[0][0]
        while start in mp:
            start = mp[start]
        return start