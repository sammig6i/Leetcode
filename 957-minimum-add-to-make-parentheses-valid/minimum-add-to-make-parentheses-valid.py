class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        opening = 0
        for c in s:
            if c == "(":
                opening += 1
            else:
                if opening:
                    opening -= 1
                else:
                    count += 1
        return count + opening
        