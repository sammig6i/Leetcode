class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0

        lps = [0] * len(needle)
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[prevLPS] == needle[i]:
                lps[i] = prevLPS + 1
                i += 1
                prevLPS += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
                
        i = 0 # haystack
        j = 0 # needle
        while i < len(haystack):
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]
            
            if j == len(needle):
                return i - len(needle)
        return -1