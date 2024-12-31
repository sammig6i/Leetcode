class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        pattern_mp = {}
        word_mp = {}
        for i in range(len(pattern)):
            if (words[i] in word_mp and word_mp[words[i]] != pattern[i] or
                pattern[i] in pattern_mp and pattern_mp[pattern[i]] != words[i]):
                return False
            pattern_mp[pattern[i]] = words[i]
            word_mp[words[i]] = pattern[i]
        return True