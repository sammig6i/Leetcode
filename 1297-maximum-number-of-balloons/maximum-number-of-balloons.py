class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countMap = {char: text.count(char) for char in set(text)}
        balloon = "balloon"
        balloonMap = {char: balloon.count(char) for char in set(balloon)}

        res = len(text)
        for c in balloonMap:
            res = min(res, countMap.get(c, 0) // balloonMap[c])
        return res



       
