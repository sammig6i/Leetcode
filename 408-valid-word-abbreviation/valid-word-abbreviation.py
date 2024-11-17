class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        w = len(word)
        a = len(abbr)

        while i < w:
            if j >= a:
                return False

            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            
            if not abbr[j].isdigit():
                return False 

            num_start = j
            while j < a and abbr[j].isdigit():
                j += 1
            num_str = abbr[num_start:j]
            if num_str[0] == "0":
                return False

            i = i + int(num_str)

        return i == w and j == a
                
        
        