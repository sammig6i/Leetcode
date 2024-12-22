class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] in vowels else 0)
        
        for i in range(k, n + 1):
            res = max(res, prefix[i] - prefix[i - k])
        return res
# prefix = [0,1,1,1,2,3,4,4,5,5]