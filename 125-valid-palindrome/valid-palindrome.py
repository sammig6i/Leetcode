class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if s[L].lower() != s[R].lower():
                if not s[L].lower().isalnum():
                    L += 1
                elif not s[R].lower().isalnum():
                    R -= 1
                else:
                    return False
            else:
                L += 1
                R -= 1
        return True

    
