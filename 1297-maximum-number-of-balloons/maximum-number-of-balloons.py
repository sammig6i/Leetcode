class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")
        word = Counter(text)

        res = float("inf")
        for c in balloon:
            if c in word:
                res = min(res, word[c] // balloon[c])
            else:
                return 0
        return res
        