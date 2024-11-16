class Solution:
    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                skipL, skipR = s[L + 1:R + 1], s[L:R]
                if skipL[::-1] == skipL or skipR[::-1] == skipR:
                    return True
                else:
                    return False
            L += 1
            R -= 1
        return True
                    

