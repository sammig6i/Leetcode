class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char_set = set()
        for c in sentence:
            char_set.add(c)
        return len(char_set) == 26
