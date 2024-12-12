class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif not abbr[j].isdigit():
                return False
            else:
                if abbr[j] == "0":
                    return False
                skip = 0
                while j < len(abbr) and abbr[j].isdigit():
                    skip = int(abbr[j]) + skip * 10
                    j += 1
                i += int(skip)
        return i == len(word) and j == len(abbr)
                