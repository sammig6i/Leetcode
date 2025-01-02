class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1 = Counter(word1)
        word2 = Counter(word2)

        sorted_word1 = sorted(word1.items(), key=lambda x: x[1])
        sorted_word2 = sorted(word2.items(), key=lambda x: x[1])

        for (c1, count1), (c2, count2) in zip(sorted_word1, sorted_word2):
            if (c1 not in word2 or
                c2 not in word1 or
                count1 != count2):
                return False
        return True