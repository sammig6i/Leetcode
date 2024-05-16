class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        wordS = {}
        wordT = {}

        for i in range(len(s)):
            wordS[s[i]] = 1 + wordS.get(s[i], 0)
            wordT[t[i]] = 1 + wordT.get(t[i], 0)

        return wordT == wordS
