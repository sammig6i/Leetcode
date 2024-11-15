class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) == 0:
            return False

        i = 0 
        j = 0
        m = len(word)
        n = len(abbr)
        while i < m:
            if j >= len(abbr):
                return False
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                if not abbr[j].isdigit():
                    return False
                num_start = j
                while j < n and abbr[j].isdigit():
                    j += 1
                num_str = abbr[num_start:j]

                if num_str[0] == '0':
                    return False
                
                i += int(num_str)
                
        return i == m and j == n
                    
