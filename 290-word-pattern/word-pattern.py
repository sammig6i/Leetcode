class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        store = set()

        for i, (c, w) in enumerate(zip(pattern, words)):
            if c in charToWord:
                if words[charToWord[c]] != w:
                    return False
            else:
                if w in store:
                    return False
                charToWord[c] = i
                store.add(w)
        return True