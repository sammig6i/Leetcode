class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countMap = Counter(text)
        balloonMap = Counter("balloon")

        res = len(text)
        for c in balloonMap:
            res = min(res, countMap[c] // balloonMap[c])
        return res



       
