class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1_count = Counter(word1)
        word2_count = Counter(word2)

        sorted_word1 = sorted(word1_count.items(), key=lambda x: x[1])
        sorted_word2 = sorted(word2_count.items(), key=lambda x: x[1])

        for (c1, count1), (c2, count2) in zip(sorted_word1, sorted_word2):
            if c1 not in word2_count or c2 not in word1_count or count1 != count2:
                return False
        return True
            