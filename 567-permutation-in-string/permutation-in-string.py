class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = Counter(s1)
        s2_counts = defaultdict(int)
        L = 0
        for R in range(len(s2)):
            c = s2[R]
            s2_counts[c] += 1

            while (R - L + 1) > len(s1):
                c = s2[L]
                s2_counts[c] -= 1
                if not s2_counts[c]:
                    del s2_counts[c]
                L += 1
            
            if s1_counts == s2_counts:
                return True
        return False