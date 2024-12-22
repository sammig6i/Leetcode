class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)
        for i in range(len(word_list)):
            if word_list[i] == ch:
                L, R = 0, i
                while L < R:
                    word_list[L], word_list[R] = word_list[R], word_list[L]
                    L += 1
                    R -= 1
                # reversed_portion = word_list[:i + 1][::-1]
                # word_list[:i + 1] = reversed_portion
                break
        return "".join(word_list)
