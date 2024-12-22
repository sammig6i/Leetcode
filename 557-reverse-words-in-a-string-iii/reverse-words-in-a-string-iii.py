class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            word = list(words[i])
            L, R = 0, len(word) - 1
            while L < R:
                word[L], word[R] = word[R], word[L]
                L += 1
                R -= 1
            words[i] = "".join(word)
        return " ".join(words)