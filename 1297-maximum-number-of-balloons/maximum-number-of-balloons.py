class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")
        word = Counter(text)

        res = float("inf")
        for c in balloon:
            if c not in word:
                return 0
            res = min(res, word[c] // balloon[c])
        return res
        