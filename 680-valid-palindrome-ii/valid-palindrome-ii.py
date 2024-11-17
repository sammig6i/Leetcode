class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(s, L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True

        L, R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return check_palindrome(s, L + 1, R) or check_palindrome(s, L, R - 1)
            else:
                L += 1
                R -= 1
        return True

            
