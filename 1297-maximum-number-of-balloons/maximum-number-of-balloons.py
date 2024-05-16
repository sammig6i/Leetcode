class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")
        word = Counter(text)

        res = len(text)

        for c in balloon:
            res = min(res, word[c] // balloon[c])
        return res

        

