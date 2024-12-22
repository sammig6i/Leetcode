class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        L, R = 0, len(s) - 1
        while L < R:
            if not s[L].isalpha():
                L += 1
            elif not s[R].isalpha():
                R -= 1
            else:
                s[L], s[R] = s[R], s[L]
                L += 1
                R -= 1
        return "".join(s)
        
# "Test1ng-Leet=code-Q!