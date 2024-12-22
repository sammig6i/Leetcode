class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        L = 0
        vowel_count = 0
        res = float("-inf")
        for R in range(len(s)):
            vowel_count += 1 if s[R] in vowels else 0
            if R - L + 1 > k:
                vowel_count -= 1 if s[L] in vowels else 0
                L += 1
            res = max(res, vowel_count)
        return res
    
# abciiidef
# vowel count = 2