class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if not self.isAlpha(s[L]):
                L += 1
            elif not self.isAlpha(s[R]):
                R -= 1
            else:
                if s[L].lower() != s[R].lower():
                    return False
                else:
                    L += 1
                    R -= 1
        return True


    def isAlpha(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('0') <= ord(c) <= ord('9') or
        ord('a') <= ord(c) <= ord('z'))