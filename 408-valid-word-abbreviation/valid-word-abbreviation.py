class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # substitution, s10n
        # apple, a2e
        # internationalization, i12iz4n

        i = j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            
            if not abbr[j].isdigit():
                return False
           
            num_start = j
            while j < len(abbr) and abbr[j].isdigit():
                j += 1
            num_str = abbr[num_start:j]
            if num_str[0] == "0":
                return False
            i += int(num_str)

        return i == len(word) and j == len(abbr)
            
            
            


