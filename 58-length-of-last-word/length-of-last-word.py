class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        while s[i] == " ":
            length = 0
            i -= 1
        while s[i] != " " and i >= 0:
            length += 1
            i -= 1
        return length

        
        
        

        