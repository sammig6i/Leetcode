class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        L = 0
        for R in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[R]) - ord('a')
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] + 1:
                matches -= 1
            
            index = ord(s2[L]) - ord('a')
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1
            L += 1
        return matches == 26

        
