class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")
        word_count = Counter(text)

        res = len(text)
        for c in balloon:
            res = min(res, word_count[c] // balloon[c])
        
        return res