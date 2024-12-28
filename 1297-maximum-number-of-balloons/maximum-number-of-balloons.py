class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = defaultdict(int)
        txt = defaultdict(int)
        for c in "balloon":
            balloon[c] += 1
        
        for c in text:
            txt[c] += 1
        
        res = float("inf")
        for c in balloon:
            if c not in txt:
                return 0
            res = min(res, txt[c] // balloon[c])
        return res


        