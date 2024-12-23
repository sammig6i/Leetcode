class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = 0

        for c in sentence:
            curr_char = ord(c) - ord("a")

            masked_bit = 1 << curr_char

            seen |= masked_bit
        return seen == (1 << 26) - 1