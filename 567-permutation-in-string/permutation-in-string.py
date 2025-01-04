class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        s2_count = defaultdict(int)
        L = 0

        for R in range(len(s2)):
            c = s2[R]
            s2_count[c] += 1

            if (R - L + 1) > len(s1):
                c = s2[L]
                s2_count[c] -= 1
                if not s2_count[c]:
                    del s2_count[c]
                L += 1
            
            if s1_count == s2_count: return True
        return False
