class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif not abbr[j].isdigit():
                return False
            else:
                num_start = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                num_str = abbr[num_start:j]
                if num_str[0] == '0':
                    return False
                i += int(num_str)
        return i == len(word) and j == len(abbr)