class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        charToWord = defaultdict(int)
        wordToChar = defaultdict(int)
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        for i, (c, w) in enumerate(zip(pattern, words)):
            if charToWord[c] != wordToChar[w]:
                return False
            charToWord[c] = i + 1
            wordToChar[w] = i + 1
        return True