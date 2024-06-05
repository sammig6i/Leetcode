class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            if not self.isAlphaNum(s[L]):
                L += 1
            elif not self.isAlphaNum(s[R]):
                R -= 1
            else:
                if (s[L].lower() != s[R].lower()):
                    return False
                R -= 1
                L += 1
        return True

    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))