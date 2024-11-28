class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if s[L].lower() != s[R].lower():
                if not self.isAlpha(s[L].lower()):
                    L += 1
                elif not self.isAlpha(s[R].lower()):
                    R -= 1
                else:
                    return False
            else:
                L += 1
                R -= 1
        return True

    def isAlpha(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

