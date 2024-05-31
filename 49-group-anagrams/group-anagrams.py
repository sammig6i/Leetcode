class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            count = [0] * 26 # a -> z
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(s)
        return res.values()
            