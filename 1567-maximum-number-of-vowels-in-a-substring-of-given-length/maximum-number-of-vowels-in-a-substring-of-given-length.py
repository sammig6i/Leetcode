class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        L = cnt = res = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for R in range(len(s)):
            cnt += 1 if s[R] in vowels else 0
            if R - L + 1 > k:
                cnt -= 1 if s[L] in vowels else 0
                L += 1
            res = max(res, cnt)

        return res