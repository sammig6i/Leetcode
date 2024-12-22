class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)
        for i in range(len(word_list)):
            if word_list[i] == ch:
                reversed_portion = word_list[:i + 1][::-1]
                word_list[:i + 1] = reversed_portion
                break
        return "".join(word_list)
