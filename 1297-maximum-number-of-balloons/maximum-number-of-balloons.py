class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countMap = Counter(text)
        balloonMap = Counter("balloon")

        res = float("inf")
        for c in balloonMap:
            res = min(res, countMap[c] // balloonMap[c])
        return res



       
