class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = defaultdict(int)

        for c in text:
            if c in "balon":
                word[c] += 1
        
        if len(word) < 5:
            return 0
        
        word["l"] //= 2
        word["o"] //= 2
        return min(word.values())


        